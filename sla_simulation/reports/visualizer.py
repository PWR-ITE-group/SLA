# Graphs and visualizations
import matplotlib.pyplot as plt

class Visualizer:
    @staticmethod
    def plot_uptime_over_time(logs):
        """Plot uptime over time."""
        timestamps = [log["timestamp"] for log in logs]
        uptimes = [log["uptime"] for log in logs]

        plt.plot(timestamps, uptimes, marker='o', label='Uptime (%)')
        plt.axhline(y=99.9, color='r', linestyle='--', label='Uptime Threshold')
        plt.xlabel('Time')
        plt.ylabel('Uptime (%)')
        plt.title('Uptime Over Time')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
