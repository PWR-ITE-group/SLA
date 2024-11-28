# Detects SLA breaches
class BreachChecker:
    @staticmethod
    def detect_breaches(logs):
        """Analyze logs to detect SLA breaches."""
        breaches = [log for log in logs if log["breach"]]
        return breaches

    @staticmethod
    def calculate_penalty(breaches, penalty_amount):
        """Calculate total penalties based on breaches."""
        return len(breaches) * penalty_amount
