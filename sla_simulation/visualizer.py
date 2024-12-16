from matplotlib import pyplot as plt


class Visualizer:
    """
    Класс для визуализации данных симуляции.
    """
    @staticmethod
    def plot_histogram_of_availability(logs, total_time):
        availability = [
            100 * (1 - (log['downtime'] / 24)) for log in logs
        ]
        plt.hist(availability, bins=15, color='skyblue', edgecolor='black')
        plt.title('Histogram of Availability (Monte Carlo Simulation)')
        plt.xlabel('Availability (%)')
        plt.ylabel('Frequency')
        plt.grid()
        plt.show()

    @staticmethod
    def plot_monthly_failures(logs):
        months = {}
        for log in logs:
            month = (log['day'] - 1) // 30 + 1
            months[month] = months.get(month, 0) + log['failures']

        plt.bar(months.keys(), months.values(), color='lightgreen', edgecolor='black')
        plt.title('Total Failures per Month')
        plt.xlabel('Month')
        plt.ylabel('Number of Failures')
        plt.show()

    @staticmethod
    def plot_daily_downtime(logs):
        days = [log['day'] for log in logs]
        downtimes = [max(0, log['downtime']) for log in logs]  # Убираем негативные значения
        plt.plot(days, downtimes, marker='o', linestyle='-', color='orange')
        plt.title('Daily Server Downtime (hours)')
        plt.xlabel('Days')
        plt.ylabel('Downtime (hours)')
        plt.grid()
        plt.show()

    @staticmethod
    def plot_total_failures(logs, title="Total Failures per Day", x_label="Days"):
        """
        Построение столбчатого графика общего количества поломок.
        Теперь поддерживает группировку по месяцам.
        """
        x = [log['month'] if 'month' in log else log['day'] for log in logs]
        y = [log['failures'] for log in logs]

        plt.bar(x, y, color='lightgreen', edgecolor='black')
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel('Number of Failures')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()

    @staticmethod
    def plot_metric_by_servers(num_servers, values, title, y_label):
        """
        Построение графика для метрик MTTR и MTBF в зависимости от количества серверов.
        """
        plt.plot(num_servers, values, marker='o', linestyle='-', color='b')
        plt.title(title)
        plt.xlabel("Number of Servers")
        plt.ylabel(y_label)
        plt.grid()
        plt.show()
