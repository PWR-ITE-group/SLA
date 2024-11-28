# Textual reports
class ReportGenerator: # TODO: consider doing reports to a txt file, maybe multiple simulations and as a result avarage stats to report
    @staticmethod
    def generate_text_report(logs, breaches):
        """Generate a textual summary of the simulation."""
        return {
            "Total Logs": len(logs),
            "Total Breaches": len(breaches),
            "Compliance Rate": f"{(1 - len(breaches) / len(logs)) * 100:.2f}%"
        }
