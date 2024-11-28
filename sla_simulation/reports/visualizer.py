from datetime import datetime
from matplotlib import pyplot as plt


class Visualizer:
    @staticmethod
    def plot_uptime_over_time(logs):
        """Plot uptime over the simulated time period."""
        timestamps = [
            datetime.strptime(log["timestamp"], "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%d")
            for log in logs
        ]
        uptimes = [log["uptime"] for log in logs]

        plt.figure(figsize=(10, 6))
        plt.plot(timestamps, uptimes, marker='o', label='Uptime (%)')
        plt.axhline(y=99.9, color='r', linestyle='--', label='Uptime Threshold')
        plt.xlabel('Date')
        plt.ylabel('Uptime (%)')
        plt.title('Uptime Over Time')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
