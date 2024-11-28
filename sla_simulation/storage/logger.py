import json

class LogStorage:
    @staticmethod
    def save_logs_to_json(logs, file_name="logs.json"):
        """Save logs to a JSON file."""
        with open(file_name, "w") as file:
            json.dump(logs, file, indent=4)

    @staticmethod
    def load_logs_from_json(file_name="logs.json"):
        """Load logs from a JSON file."""
        with open(file_name, "r") as file:
            return json.load(file)
