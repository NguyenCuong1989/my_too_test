class ObservationAggregator:
    def __init__(self, event_bus, telemetry):
        self.event_bus = event_bus
        self.telemetry = telemetry
    def collect(self):
        observations = {"events": [], "metrics": self.telemetry.metrics}
        while True:
            event = self.event_bus.consume()
            if event is None: break
            observations["events"].append(event)
        return observations
