class SLAContract:
    """
    Класс для хранения параметров одного SLA-контракта.
    """
    def __init__(self, name, num_servers, disk_quality, availability_target,
                 max_failure_time, max_failures, daily_cost, penalty_cost):
        self.name = name
        self.num_servers = num_servers
        self.disk_quality = disk_quality
        self.availability_target = availability_target
        self.max_failure_time = max_failure_time
        self.max_failures = max_failures
        self.daily_cost = daily_cost
        self.penalty_cost = penalty_cost

    def display_info(self):
        print(f"SLA Plan: {self.name}")
        print(f"  Number of Servers: {self.num_servers}")
        print(f"  Disk Quality: {self.disk_quality}")
        print(f"  Availability Target: {self.availability_target}%")
        print(f"  Max Failure Time: {self.max_failure_time} hours")
        print(f"  Max Failures Allowed: {self.max_failures}")
        print(f"  Daily Cost: ${self.daily_cost}")
        print(f"  Penalty per Violation: ${self.penalty_cost}")
        print("---------------------------------------")