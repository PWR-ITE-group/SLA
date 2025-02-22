import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass
class ServiceMetrics:
    uptime_percentage: float
    mean_recovery_time: float
    mean_operational_time: float
    incident_count: float
    outage_duration: float
    total_expenses: float
    sla_violation_cost: float


class InfrastructureSimulator:
    def __init__(self, unit_count: int, reliability_alpha: float,
                 reliability_beta: float, fix_time_mean: float):
        self.unit_count = unit_count
        self.reliability_alpha = reliability_alpha
        self.reliability_beta = reliability_beta
        self.fix_time_mean = fix_time_mean

        self._init_monitoring_system()

    def _init_monitoring_system(self):
        self.operational_units = np.ones(self.unit_count)
        self.next_failure = self._forecast_failures()
        self.recovery_completion = np.zeros(self.unit_count)

        self.accumulated_downtime = 0
        self.accumulated_uptime = 0
        self.incident_tracker = 0

    def _forecast_failures(self) -> np.ndarray:
        return (np.random.weibull(self.reliability_alpha, self.unit_count)
                * self.reliability_beta)

    def _estimate_recovery(self) -> float:
        return np.random.exponential(1 / self.fix_time_mean)

    def update_system_state(self, current_timestamp: float, interval: float):
        system_degraded = False

        for idx in range(self.unit_count):
            if self.operational_units[idx] == 1:
                if self.next_failure[idx] <= current_timestamp:
                    self.operational_units[idx] = 0
                    self.recovery_completion[idx] = (current_timestamp +
                                                     self._estimate_recovery())
            else:
                system_degraded = True
                if self.recovery_completion[idx] <= current_timestamp:
                    self.operational_units[idx] = 1
                    self.next_failure[idx] = (current_timestamp +
                                              np.random.weibull(self.reliability_alpha) *
                                              self.reliability_beta)
                    self.incident_tracker += 1

        if system_degraded:
            self.accumulated_downtime += interval
        else:
            self.accumulated_uptime += interval

    def calculate_reliability_metrics(self, duration: float) -> Tuple[float, float]:
        if self.incident_tracker == 0:
            return duration, 0

        avg_uptime = self.accumulated_uptime / self.incident_tracker
        avg_downtime = self.accumulated_downtime / self.incident_tracker
        return avg_uptime, avg_downtime


class ServiceLevelAgreement:
    def __init__(self, requirements: Dict):
        self.uptime_target = requirements['uptime_target']
        self.incident_limit = requirements['incident_limit']
        self.downtime_limit = requirements['downtime_limit']
        self.base_cost = requirements['base_cost']
        self.violation_fee = requirements['violation_fee']


def run_simulation(sim: InfrastructureSimulator, duration: float,
                   interval: float) -> InfrastructureSimulator:
    current_time = 0
    while current_time < duration:
        sim.update_system_state(current_time, interval)
        current_time += interval
    return sim


def assess_performance(sim: InfrastructureSimulator, duration: float,
                       sla: ServiceLevelAgreement) -> ServiceMetrics:
    avg_uptime, avg_downtime = sim.calculate_reliability_metrics(duration)

    if avg_uptime + avg_downtime > 0:
        availability = (avg_uptime / (avg_uptime + avg_downtime)) * 100
    else:
        availability = 0

    penalty = (sla.violation_fee if availability < sla.uptime_target else 0)

    return ServiceMetrics(
        uptime_percentage=availability,
        mean_recovery_time=avg_downtime,
        mean_operational_time=avg_uptime,
        incident_count=sim.incident_tracker,
        outage_duration=sim.accumulated_downtime,
        total_expenses=sla.base_cost + penalty,
        sla_violation_cost=penalty
    )


def perform_statistical_analysis(config: dict, trials: int) -> Tuple[Dict, Dict]:
    metrics_collection = {
        metric: [] for metric in [
            'uptime_percentage', 'mean_recovery_time', 'mean_operational_time',
            'incident_count', 'outage_duration', 'total_expenses',
            'sla_violation_cost'
        ]
    }

    success_tracking = {
        'uptime': 0, 'incidents': 0, 'downtime': 0
    }

    sla = ServiceLevelAgreement({
        'uptime_target': config['sla_level'],
        'incident_limit': config['max_incidents'],
        'downtime_limit': config['max_outage'],
        'base_cost': config['service_cost'],
        'violation_fee': config['breach_penalty']
    })

    for _ in range(trials):
        sim = InfrastructureSimulator(
            config['units'], config['shape'], config['scale'],
            config['recovery_rate']
        )
        sim = run_simulation(sim, config['duration'], config['step'])
        results = assess_performance(sim, config['duration'], sla)

        for metric, value in vars(results).items():
            metrics_collection[metric].append(value)

        if results.uptime_percentage >= sla.uptime_target:
            success_tracking['uptime'] += 1
        if results.incident_count <= sla.incident_limit:
            success_tracking['incidents'] += 1
        if results.outage_duration <= sla.downtime_limit:
            success_tracking['downtime'] += 1

    success_rates = {
        key: (count / trials) * 100
        for key, count in success_tracking.items()
    }

    statistics = {
        metric: {
            'mean': np.mean(values),
            'std': np.std(values)
        }
        for metric, values in metrics_collection.items()
    }

    return metrics_collection, statistics, success_rates


if __name__ == "__main__":
    simulation_config = {
        'units': 100,
        'shape': 2,
        'scale': 1200 * 24,
        'recovery_rate': 1 / 1.5,
        'duration': 8760,
        'step': 1,
        'sla_level': 90.0,
        'max_incidents': 50,
        'max_outage': 200,
        'service_cost': 1000000,
        'breach_penalty': 500000
    }
    # simulation_config = {
    #     'units': 100,
    #     'shape': 2,
    #     'scale': 1200 * 36,
    #     'recovery_rate': 1 / 3,
    #     'duration': 8760,
    #     'step': 0.1,
    #     'sla_level': 99.9,
    #     'max_incidents': 10,
    #     'max_outage': 50,
    #     'service_cost': 3000000,
    #     'breach_penalty': 1500000
    # }
    # simulation_config = {
    #      'units': 100,
    #     'shape': 2,
    #     'scale': 1200 * 48,
    #     'recovery_rate': 1 / 5,
    #     'duration': 8760,
    #     'step': 0.1,
    #     'sla_level': 99.99,
    #     'max_incidents': 5,
    #     'max_outage': 10,
    #     'service_cost': 5000000,
    #     'breach_penalty': 3000000
    # }

    collected_data, statistical_data, success_data = perform_statistical_analysis(
        simulation_config, 100
    )

    print("\nStatistical Analysis Results:")
    for metric, stats in statistical_data.items():
        print(f"{metric}: mean={stats['mean']:.2f}, std={stats['std']:.2f}")

    print("\nSuccess Rates (%):")
    for criterion, rate in success_data.items():
        print(f"{criterion}: {rate:.2f}%")

    plt.figure(figsize=(10, 6))
    plt.hist(collected_data["uptime_percentage"], bins=30,
             edgecolor="black", alpha=0.7)
    plt.title("System Availability Distribution")
    plt.xlabel("Availability (%)")
    plt.ylabel("Frequency")
    plt.grid(True, alpha=0.3)
    plt.show()
