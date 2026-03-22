# Σ_APΩ₂ CORE MODULE
# Authority: BỐ CƯỐNG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL

    def _reinit_llm(self):
        """Re-initialize LLM with current active key from KeyManager."""
        self.api_key = self.key_manager.get_active_key()
        if self.api_key:
            try:
                import google.generativeai as genai
                genai.configure(api_key=self.api_key)
                from langchain_google_genai import ChatGoogleGenerativeAI
                self.llm = ChatGoogleGenerativeAI(
                    model="gemini-1.5-flash",
                    temperature=0.0,
                    google_api_key=self.api_key
                )
                self.logger.info(f"🔄 LLM re-initialized with new key index.")
                return True
            except Exception as e:
                self.logger.error(f"Failed to re-init LLM: {e}")
        return False

    def invoke_with_retry(self, prompt, max_retries=2):
        """Invoke LLM with automatic key rotation on Quota error (429)."""
        for attempt in range(max_retries + 1):
            try:
                if not self.llm:
                    if not self._reinit_llm(): return None
                return self.llm.invoke(prompt)
            except Exception as e:
                if "429" in str(e) or "Resource has been exhausted" in str(e):
                    self.logger.warning(f"⚠️ Quota Exhausted (429). Attempting rotation {attempt+1}/{max_retries}...")
                    self.key_manager.rotate_key()
                    self._reinit_llm()
                else:
                    self.logger.error(f"LLM Error: {e}")
                    break
        return None
