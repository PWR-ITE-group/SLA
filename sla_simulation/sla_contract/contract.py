# Handles contract creation and validation
class SLAContract:
    def __init__(self, provider, client, uptime_threshold, response_time_threshold, penalties):
        self.provider = provider
        self.client = client
        self.uptime_threshold = uptime_threshold
        self.response_time_threshold = response_time_threshold
        self.penalties = penalties

    def validate_contract(self):
        """Validate the SLA contract details."""
        if not (0 <= self.uptime_threshold <= 100):
            raise ValueError("Uptime threshold must be between 0 and 100.")
        if not isinstance(self.response_time_threshold, int):
            raise ValueError("Response time threshold must be an integer (in hours).")
        return True

    def display_contract(self):
        """Display the contract details."""
        return {
            "Provider": self.provider,
            "Client": self.client,
            "Uptime Threshold (%)": self.uptime_threshold,
            "Response Time Threshold (hours)": self.response_time_threshold,
            "Penalties": self.penalties,
        }
