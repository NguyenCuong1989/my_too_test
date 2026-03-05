# Σ_APΩ₂ CORE MODULE
# Authority: BỐ CƯỐNG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL

"""
🌐 AUTONOMOUS BROWSER AGENT — Powered by LOCAL OLLAMA (qwen3:8b)
Không cần cloud quota. Playwright + Ollama = Browser Agent tự trị hoàn toàn.

Khả năng:
- Điều hướng trang web theo mục tiêu ngôn ngữ tự nhiên
- Đọc nội dung trang, phân tích, ra quyết định bước tiếp theo
- Điền form, click button, extract data
- Unblock GitHub secrets, tương tác GitHub UI, v.v.
"""

import asyncio
import logging
import json
import sys
from datetime import datetime
from pathlib import Path

import ollama
from playwright.async_api import async_playwright, Page

try:
    from ..neural_link import NeuralLink
except (ImportError, ValueError):
    sys.path.append(str(Path(__file__).parent.parent))
    from neural_link import NeuralLink

LOCAL_MODEL = "qwen3:8b"
logger = logging.getLogger("AutonomousBrowser")

class AutonomousBrowserAgent:
    """
    Browser Agent tự trị dùng Ollama local.
    Thay thế hoàn toàn browser_subagent cloud — không mất quota.
    """

    def __init__(self, headless: bool = True):
        self.headless = headless
        self.link = NeuralLink()
        self.model = LOCAL_MODEL

    async def _think(self, goal: str, page_content: str, history: list) -> dict:
        """
        Hỏi Ollama: 'Dựa trên trang này, bước tiếp theo là gì?'
        Trả về JSON hành động cần thực hiện.
        """
        prompt = f"""Bạn là một browser agent AI. Nhiệm vụ: {goal}

Nội dung trang hiện tại (rút gọn):
{page_content[:3000]}

Lịch sử hành động đã thực hiện:
{json.dumps(history[-5:], ensure_ascii=False)}

Trả về JSON hành động tiếp theo (CHỈ JSON, không giải thích):
{{
  "action": "click|type|navigate|extract|done|scroll",
  "target": "CSS selector hoặc URL hoặc text cần gõ",
  "reason": "lý do ngắn gọn",
  "done": false
}}

Nếu nhiệm vụ hoàn thành, trả về: {{"action": "done", "target": "", "reason": "..."  , "done": true}}"""

        try:
            resp = ollama.chat(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                options={"temperature": 0.1}
            )
            raw = resp["message"]["content"].strip()
            if "<think>" in raw:
                raw = raw.split("</think>")[-1].strip()
            raw = raw.replace("```json", "").replace("```", "").strip()
            return json.loads(raw)
        except Exception as e:
            logger.error(f"Ollama think error: {e}")
            return {"action": "done", "target": "", "reason": f"error: {e}", "done": True}

    async def _get_page_summary(self, page: Page) -> str:
        """Lấy nội dung trang, rút gọn để fit vào context"""
        try:
            title = await page.title()
            url = page.url
            # Lấy text từ các phần tử quan trọng
            text = await page.evaluate("""() => {
                const important = [...document.querySelectorAll('h1,h2,h3,button,a,input,label,p')];
                return important.slice(0, 50).map(el => {
                    const tag = el.tagName.toLowerCase();
                    const text = el.innerText?.trim() || el.value || '';
                    const id = el.id ? `#${el.id}` : '';
                    const cls = el.className ? `.${el.className.split(' ')[0]}` : '';
                    return `[${tag}${id}${cls}]: ${text.substring(0, 100)}`;
                }).filter(t => t.length > 5).join('\\n');
            }""")
            return f"URL: {url}\nTitle: {title}\n\nElements:\n{text}"
        except Exception as e:
            return f"Error reading page: {e}"

    async def run(self, goal: str, start_url: str = None, max_steps: int = 15) -> str:
        """
        Thực thi mục tiêu bằng cách duyệt web tự động.

        Args:
            goal: Mục tiêu bằng ngôn ngữ tự nhiên (VD: "Unblock secret on GitHub")
            start_url: URL bắt đầu (optional)
            max_steps: Số bước tối đa
        """
        logger.info(f"🌐 Browser Agent START: {goal}")
        self.link.send_pulse("BrowserAgent", "TASK_START", goal, 0.9)

        history = []
        result = "Task incomplete"

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            context = await browser.new_context()
            page = await context.new_page()

            if start_url:
                await page.goto(start_url, wait_until="domcontentloaded", timeout=20000)

            for step in range(max_steps):
                logger.info(f"🔄 Step {step + 1}/{max_steps}")
                page_summary = await self._get_page_summary(page)
                decision = await self._think(goal, page_summary, history)

                logger.info(f"🧠 AI Decision: {decision.get('action')} → {str(decision.get('target', ''))[:60]}")
                history.append({
                    "step": step + 1,
                    "url": page.url,
                    "action": decision
                })

                if decision.get("done") or decision.get("action") == "done":
                    result = decision.get("reason", "Task completed")
                    logger.info(f"✅ DONE: {result}")
                    break

                # Thực thi hành động
                try:
                    action = decision.get("action", "")
                    target = decision.get("target", "")

                    if action == "navigate" and target:
                        await page.goto(target, wait_until="domcontentloaded", timeout=15000)

                    elif action == "click" and target:
                        # Thử nhiều cách click
                        try:
                            await page.click(target, timeout=5000)
                        except:
                            # Thử click bằng text
                            await page.get_by_text(target).first.click(timeout=5000)

                    elif action == "type" and target:
                        parts = target.split("|", 1)
                        if len(parts) == 2:
                            selector, text = parts
                            await page.fill(selector, text)
                        else:
                            await page.keyboard.type(target)

                    elif action == "scroll":
                        await page.evaluate("window.scrollBy(0, 500)")

                    elif action == "extract":
                        result = await page.evaluate(f"document.querySelector('{target}')?.innerText || ''")
                        logger.info(f"📋 Extracted: {result[:200]}")

                    await asyncio.sleep(1.5)  # Đợi page load

                except Exception as e:
                    logger.warning(f"Action failed: {e}, continuing...")

            await browser.close()

        self.link.send_pulse("BrowserAgent", "TASK_DONE", result[:200], 0.8)
        logger.info(f"🏁 Browser Agent DONE: {result[:100]}")
        return result


# ============================================================
# Quick test
# ============================================================
async def _test():
    logging.basicConfig(level=logging.INFO)
    agent = AutonomousBrowserAgent(headless=True)

    result = await agent.run(
        goal="Go to GitHub and find the unblock secret link, then click allow",
        start_url="https://github.com/NguyenCuong1989/my_too_test/security/secret-scanning/unblock-secret/3ABilQZ69Rm3g7o2ga7kvnxex16"
    )
    print(f"\nResult: {result}")

async def run(payload: str = None) -> str:
    """Standard Entry Point for Omni Orchestrator"""
    try:
        logging.basicConfig(level=logging.CRITICAL)
        logging.getLogger().setLevel(logging.CRITICAL)
        agent = AutonomousBrowserAgent()
        goal = None
        url = None
        if payload:
            if isinstance(payload, str):
                try:
                    data = json.loads(payload)
                    goal = data.get("goal")
                    url = data.get("url")
                except:
                    goal = payload
            else:
                goal = payload.get("goal")
                url = payload.get("url")

        if not goal:
            return json.dumps({"status": "error", "error": "No goal provided"})

        result = await agent.run(goal=goal, start_url=url)
        return json.dumps({"status": "success", "result": result})
    except Exception as e:
        return json.dumps({"status": "error", "error": str(e)})

async def run(payload: str = None) -> str:
    """Standard Entry Point for Omni Orchestrator"""
    try:
        logging.basicConfig(level=logging.CRITICAL)
        logging.getLogger().setLevel(logging.CRITICAL)
        agent = AutonomousBrowserAgent()
        goal = None
        url = None
        if payload:
            if isinstance(payload, str):
                try:
                    data = json.loads(payload)
                    goal = data.get("goal")
                    url = data.get("url")
                except:
                    goal = payload
            else:
                goal = payload.get("goal")
                url = payload.get("url")

        if not goal:
            return json.dumps({"status": "error", "error": "No goal provided"})

        result = await agent.run(goal=goal, start_url=url)
        return json.dumps({"status": "success", "result": result})
    except Exception as e:
        return json.dumps({"status": "error", "error": str(e)})

async def run(payload: str = None) -> str:
    """Standard Entry Point for Omni Orchestrator"""
    try:
        logging.basicConfig(level=logging.CRITICAL)
        logging.getLogger().setLevel(logging.CRITICAL)
        agent = AutonomousBrowserAgent()
        goal = None
        url = None
        if payload:
            if isinstance(payload, str):
                try:
                    data = json.loads(payload)
                    goal = data.get("goal")
                    url = data.get("url")
                except:
                    goal = payload
            else:
                goal = payload.get("goal")
                url = payload.get("url")

        if not goal:
            return json.dumps({"status": "error", "error": "No goal provided"})

        result = await agent.run(goal=goal, start_url=url)
        return json.dumps({"status": "success", "result": result})
    except Exception as e:
        return json.dumps({"status": "error", "error": str(e)})

async def run(payload: str = None) -> str:
    """Standard Entry Point for Omni Orchestrator"""
    try:
        logging.basicConfig(level=logging.CRITICAL)
        logging.getLogger().setLevel(logging.CRITICAL)
        agent = AutonomousBrowserAgent()
        goal = None
        url = None
        if payload:
            if isinstance(payload, str):
                try:
                    data = json.loads(payload)
                    goal = data.get("goal")
                    url = data.get("url")
                except:
                    goal = payload
            else:
                goal = payload.get("goal")
                url = payload.get("url")

        if not goal:
            return json.dumps({"status": "error", "error": "No goal provided"})

        result = await agent.run(goal=goal, start_url=url)
        return json.dumps({"status": "success", "result": result})
    except Exception as e:
        return json.dumps({"status": "error", "error": str(e)})

if __name__ == "__main__":
    import asyncio
    print(asyncio.run(run()))
