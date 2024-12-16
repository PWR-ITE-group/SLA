import numpy as np
import matplotlib.pyplot as plt

class SimulationEngine:
    """
    Класс для выполнения симуляции работы серверов по SLA-контракту.
    """
    def __init__(self, sla_contract, duration_days):
        self.sla_contract = sla_contract
        self.duration_days = duration_days
        self.logs = []

    def simulate_failures(self):
        """
        Генерация данных о времени простоя и поломках для серверов с нормальным распределением.
        """
        mean_failure_time = self.sla_contract.max_failure_time / 2
        std_dev_failure_time = mean_failure_time / 3

        for day in range(1, self.duration_days + 1):
            daily_downtime = 0
            failures = 0

            for _ in range(self.sla_contract.num_servers):
                if np.random.random() > self.sla_contract.availability_target / 100:
                    failure_time = max(0, np.random.normal(mean_failure_time, std_dev_failure_time))
                    daily_downtime += failure_time
                    failures += 1

            self.logs.append({
                'day': day,
                'downtime': daily_downtime,
                'failures': failures
            })

    def get_logs(self):
        return self.logs
