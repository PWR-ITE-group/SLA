# Core simulation logic
import random
from datetime import datetime

class SimulationEngine:
    def __init__(self, sla_contract):
        self.sla_contract = sla_contract
        self.logs = []

    def run_simulation(self, duration_in_days):
        """Simulate service metrics for the specified duration."""
        for day in range(duration_in_days):
            uptime = random.uniform(95, 100)  # Random uptime percentage
            response_time = random.randint(1, 48)  # Random response time (in hours)
            breach = uptime < self.sla_contract.uptime_threshold or \
                     response_time > self.sla_contract.response_time_threshold

            self.logs.append({
                "timestamp": datetime.now().isoformat(),
                "uptime": uptime,
                "response_time": response_time,
                "breach": breach
            })

    def get_logs(self):
        """Return simulation logs."""
        return self.logs
