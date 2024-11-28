import sqlite3

class Database:
    def __init__(self, db_name="sla_logs.db"):
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """Create database tables."""
        with self.connection:
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS Logs (
                    id INTEGER PRIMARY KEY,
                    timestamp TEXT,
                    uptime REAL,
                    response_time INTEGER,
                    breach BOOLEAN
                );
            """)

    def save_log(self, log):
        """Save a single log to the database."""
        with self.connection:
            self.connection.execute("""
                INSERT INTO Logs (timestamp, uptime, response_time, breach)
                VALUES (?, ?, ?, ?);
            """, (log["timestamp"], log["uptime"], log["response_time"], log["breach"]))

    def fetch_all_logs(self):
        """Fetch all logs from the database."""
        with self.connection:
            return self.connection.execute("SELECT * FROM Logs").fetchall()
