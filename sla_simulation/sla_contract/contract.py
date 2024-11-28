from datetime import datetime

class SLAContract:
    def __init__(self, provider, client, start_date, end_date, uptime_threshold, response_time_threshold, penalties):
        self.provider = provider
        self.client = client
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
        self.uptime_threshold = uptime_threshold
        self.response_time_threshold = response_time_threshold
        self.penalties = penalties

    def validate_contract(self):
        """Validate the SLA contract details."""
        if not (0 <= self.uptime_threshold <= 100):
            raise ValueError("Uptime threshold must be between 0 and 100.")
        if not isinstance(self.response_time_threshold, int):
            raise ValueError("Response time threshold must be an integer (in hours).")
        if self.start_date >= self.end_date:
            raise ValueError("Start date must be before end date.")
        return True

    def display_contract(self):
        """Display the contract details."""
        return {
            "Provider": self.provider,
            "Client": self.client,
            "Start Date": self.start_date.strftime("%Y-%m-%d"),
            "End Date": self.end_date.strftime("%Y-%m-%d"),
            "Uptime Threshold (%)": self.uptime_threshold,
            "Response Time Threshold (hours)": self.response_time_threshold,
            "Penalties": self.penalties,
        }
