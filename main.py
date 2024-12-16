from sla_simulation.contracts import SLAContract
from sla_simulation.metrics import MetricsCalculator
from sla_simulation.simulation import SimulationEngine
from sla_simulation.visualizer import Visualizer

def group_logs_by_month(logs, days_in_month=30):
    """
    Группирует логи по месяцам, суммируя поломки и простои.
    """
    monthly_logs = []
    for month in range(0, len(logs), days_in_month):
        monthly_failures = sum(log['failures'] for log in logs[month:month + days_in_month])
        monthly_downtime = sum(log['downtime'] for log in logs[month:month + days_in_month])
        monthly_logs.append({'month': (month // days_in_month) + 1,
                             'failures': monthly_failures,
                             'downtime': monthly_downtime})
    return monthly_logs

if __name__ == "__main__":
    # Создаем SLA-контракты
    premium_sla = SLAContract("Premium", num_servers=5, disk_quality="High", availability_target=99.9,
                              max_failure_time=1, max_failures=2, daily_cost=200, penalty_cost=500)

    # Выводим информацию о контракте
    premium_sla.display_info()

    # Симулируем работу для SLA
    duration = 360  # 360 дней
    engine = SimulationEngine(premium_sla, duration)
    engine.simulate_failures()

    # Получаем логи и рассчитываем метрики
    logs = engine.get_logs()
    print("Metrics for Premium SLA:")
    print(f"  Mean Time to Repair (MTTR): {MetricsCalculator.calculate_mttr(logs):.2f} hours")
    print(f"  Mean Time Between Failures (MTBF): {MetricsCalculator.calculate_mtbf(logs, duration):.2f} days")
    print(f"  Average Downtime: {MetricsCalculator.calculate_average_downtime(logs):.2f} hours/day")
    print(f"  Total Failures: {MetricsCalculator.calculate_total_failures(logs)}")

    # Визуализация данных
    total_time = duration * 24  # Общее количество часов за весь период
    Visualizer.plot_histogram_of_availability(logs, total_time)
    Visualizer.plot_daily_downtime(logs)

    # Группируем логи по месяцам и строим график
    monthly_logs = group_logs_by_month(logs)
    Visualizer.plot_total_failures(monthly_logs, title="Total Failures per Month", x_label="Months")
