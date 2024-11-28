from datetime import datetime, timedelta
import random

class SimulationEngine:
    def __init__(self, sla_contract):
        self.sla_contract = sla_contract
        self.logs = []

    def run_simulation(self):
        """
        Simulate service performance over the agreed SLA period.
        Generate one log entry per day, starting from the contract's start date.
        """
        start_date = self.sla_contract.start_date
        end_date = self.sla_contract.end_date
        current_date = start_date

        while current_date <= end_date:
            uptime = random.uniform(95, 100)  # Simulated uptime percentage
            response_time = random.randint(1, 48)  # Simulated response time (in hours)
            breach = (
                uptime < self.sla_contract.uptime_threshold or
                response_time > self.sla_contract.response_time_threshold
            )

            self.logs.append({
                "timestamp": current_date.isoformat(),
                "uptime": uptime,
                "response_time": response_time,
                "breach": breach
            })

            # Increment to the next day
            current_date += timedelta(days=1)

    def get_logs(self):
        """Return simulation logs."""
        return self.logs
