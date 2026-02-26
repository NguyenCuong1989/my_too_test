"""
💰 REVENUE NODE — Kiếm tiền tự động
Node này tìm kiếm và thực hiện công việc để tạo ra thu nhập cho Master.
Chiến lược:
1. Upwork/Freelancer: Tìm gig AI/automation phù hợp
2. Content Generation: Tạo và đăng bài theo lịch tự động
3. Lead Outreach: Tự động tiếp cận khách hàng tiềm năng
"""

import logging
import asyncio
import json
import sys
from datetime import datetime
from pathlib import Path

try:
    from ..neural_link import NeuralLink
    from ..distributed_cluster import cluster
except (ImportError, ValueError):
    sys.path.append(str(Path(__file__).parent.parent))
    from neural_link import NeuralLink
    from distributed_cluster import cluster

# --- SERVICE PROFILES (Master's sellable skills) ---
SKILL_PROFILE = """
Master: alpha_prime_omega (Nguyễn Đức Cường)
Chuyên môn:
- AI Agent Development (Python, LangChain, CrewAI, Ollama)
- Autonomous AI Systems & Orchestration
- Web Automation (Playwright, Selenium)
- API Integration & Workflow Automation
- Notion / Airtable / Zapier Automation
- Full-stack Apps (Replit, Vercel, Netlify)
- Data Analysis & AI-powered Dashboards
Giá: Linh hoạt, thương lượng
Portfolio: DAIOF-Framework (github.com/NguyenCuong1989/DAIOF-Framework)
"""

class RevenueNode:
    """Node tự động tạo cơ hội kiếm tiền cho Master"""

    def __init__(self):
        self.logger = logging.getLogger("RevenueNode")
        self.link = NeuralLink()

    async def run_cycle(self):
        self.logger.info("💰 RevenueNode: Scanning for income opportunities...")
        await self.generate_proposal()
        await self.generate_content()

    async def generate_proposal(self):
        """Dùng 120B để tạo proposal chuyên nghiệp cho freelance jobs"""
        # Trong thực tế sẽ scrape Upwork/Toptal, nhưng demo với prompt
        job_description = """
        Looking for an AI developer to build an autonomous email processing
        system with AI analysis and CRM integration. Budget: $500-2000.
        Timeline: 2 weeks.
        """
        prompt = f"""
        {SKILL_PROFILE}

        Viết một proposal freelance chuyên nghiệp, ngắn gọn (150 từ) cho job sau:
        {job_description}

        Viết bằng tiếng Anh, giọng tự tin, nhấn mạnh DAIOF-Framework làm portfolio.
        """

        self.logger.info("📝 Generating proposal with AI cluster...")
        proposal = await cluster.route_task(prompt, complexity="complex")

        if proposal:
            self.logger.info(f"✅ Proposal generated ({len(proposal)} chars)")
            # Lưu proposal vào hệ thống
            self.link.add_autonomous_task(
                title=f"Send Proposal: AI Email System ({datetime.now().strftime('%Y-%m-%d')})",
                description=proposal[:500],
                action="Review and send via Upwork/Email",
                priority=1  # HIGH
            )
            self.link.send_pulse(
                node_name="RevenueNode",
                pulse_type="PROPOSAL_GENERATED",
                content=f"New freelance proposal ready for review",
                intensity=0.9
            )

    async def generate_content(self):
        """Tạo nội dung marketing về DAIOF để thu hút khách hàng"""
        prompt = f"""
        {SKILL_PROFILE}

        Viết 1 post LinkedIn ngắn (100 từ) về DAIOF-Framework.
        Nhấn mạnh: autonomous AI, self-healing, 18+ service integrations.
        Kết thúc bằng CTA mời collaboration.
        Viết bằng tiếng Việt, giọng tự hào và chuyên nghiệp.
        """

        content = await cluster.route_task(prompt, complexity="simple")

        if content:
            self.logger.info(f"📢 Content piece generated: {content[:80]}...")
            self.link.add_autonomous_task(
                title=f"Post LinkedIn Content ({datetime.now().strftime('%Y-%m-%d')})",
                description=content[:500],
                action="Review and post on LinkedIn",
                priority=2  # MEDIUM
            )

if __name__ == "__main__":
    async def test():
        logging.basicConfig(level=logging.INFO)
        node = RevenueNode()
        await node.run_cycle()

    asyncio.run(test())
