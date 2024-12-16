
class MetricsCalculator:
    """
    Класс для расчета метрик на основе логов симуляции.
    """
    @staticmethod
    def calculate_mttr(logs):
        total_downtime = sum(log['downtime'] for log in logs)
        total_failures = sum(log['failures'] for log in logs)
        return total_downtime / total_failures if total_failures > 0 else 0

    @staticmethod
    def calculate_mtbf(logs, duration_days):
        total_failures = sum(log['failures'] for log in logs)
        return duration_days / total_failures if total_failures > 0 else float('inf')

    @staticmethod
    def calculate_average_downtime(logs):
        return sum(log['downtime'] for log in logs) / len(logs)

    @staticmethod
    def calculate_total_failures(logs):
        return sum(log['failures'] for log in logs)

import matplotlib.pyplot as plt
