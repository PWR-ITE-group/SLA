from sla_contract.contract import SLAContract
from simulation.engine import SimulationEngine
from simulation.breach_checker import BreachChecker
from storage.logger import LogStorage
from reports.report_generator import ReportGenerator
from reports.visualizer import Visualizer

# 1. Create SLA contract
contract = SLAContract( # TODO: verify if all the data needed for SLA is here
    provider="Provider A",
    client="Client B",
    start_date="2024-11-01",
    end_date="2024-11-07",
    uptime_threshold=99.9,
    response_time_threshold=24,
    penalties=500
)
contract.validate_contract()

# 2. Run simulation
engine = SimulationEngine(contract)
engine.run_simulation()
logs = engine.get_logs()

# 3. Detect breaches
breaches = BreachChecker.detect_breaches(logs)
total_penalty = BreachChecker.calculate_penalty(breaches, contract.penalties)

# 4. Save logs
LogStorage.save_logs_to_json(logs)

# 5. Generate report
report = ReportGenerator.generate_text_report(logs, breaches)
print("Simulation Report:", report)

# 6. Visualize logs
Visualizer.plot_uptime_over_time(logs)
