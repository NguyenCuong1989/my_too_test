class CapabilityRegistry:
    def __init__(self):
        self.capabilities = {}
    def register(self, capability_id, descriptor):
        self.capabilities[capability_id] = descriptor
    def get(self, capability_id):
        return self.capabilities.get(capability_id)
    def list_capabilities(self):
        return list(self.capabilities.keys())
