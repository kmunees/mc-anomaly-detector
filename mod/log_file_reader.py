import os

from logger_configuration import logger



#Get logger
logger = logger()


def chunk_log_content(content: str):
    chunks = content.splitlines()
    return [chunk for chunk in chunks if chunk.strip()]


class LogFileListener:
    def __init__(self, folder_to_watch):
        self.folder_to_watch = folder_to_watch
        self.processed_files = set()

    def read_logs_from_files(self):
        # List all .log files in the directory
        for filename in os.listdir(self.folder_to_watch):
            file_path = os.path.join(self.folder_to_watch, filename)

            if os.path.isfile(file_path) and filename.endswith('.log'):
                # Only process new files that haven't been processed yet
                if file_path not in self.processed_files:
                    self.processed_files.add(file_path)
                    logger.info(f"New log file detected: {file_path}")
                    try:
                        with open(file_path, 'r') as file:
                            content = file.read()
                            chunks = chunk_log_content(content)
                            return chunks
                    except Exception as e:
                        logger.error(f"Error reading file {file_path}: {e}")


def detect_anomaly_by_pattern():
    return  list('')


def anomaly_detection_pattern():
    return """
    {
  "data": [
    {
      "description": "Availability anomaly - Service outage detected",
      "type": "anomaly",
      "category": "Availability",
      "severity": "high",
      "log_source": "application",
      "log_type": "WARN",
      "pattern": {
        "expression": ".*service outage detected.*",
        "conditions": [
          {
            "field": "message",
            "condition": "service outage",
            "comparison": "contains"
          }
        ]
      },
      "examples": [
        {
          "log_entry": "All services are running normally. No errors detected at this time",
          "expected_behavior": "No action required, services are operational."
        },
        {
          "log_entry": "Temporary service outage detected for 'EmailService'. Investigating further",
          "expected_behavior": "Flag anomaly, notify operations team for immediate investigation."
        }
      ],
      "action": {
        "flag": true,
        "notification": "Email",
        "severity_threshold": "high"
      }
    },
    {
      "description": "Security anomaly - Unauthorized access attempt",
      "type": "anomaly",
      "category": "Security",
      "severity": "medium",
      "log_source": "application",
      "log_type": "ERROR",
      "pattern": {
        "expression": ".*AccessDeniedException.*",
        "conditions": [
          {
            "field": "message",
            "condition": "AccessDeniedException",
            "comparison": "contains"
          }
        ]
      },
      "examples": [
        {
          "log_entry": "User login successful for username 'dave' from IP 198.51.100.25",
          "expected_behavior": "No action required, user login is legitimate."
        },
        {
          "log_entry": "AccessDeniedException: Unauthorized access attempt detected for sensitive endpoint",
          "expected_behavior": "Flag anomaly, notify security team."
        }
      ],
      "action": {
        "flag": true,
        "notification": "Slack",
        "severity_threshold": "medium"
      }
    },
    {
      "description": "Cost Efficiency anomaly - High memory usage",
      "type": "anomaly",
      "category": "Cost Efficiency",
      "severity": "medium",
      "log_source": "infrastructure",
      "log_type": "WARN",
      "pattern": {
        "expression": ".*Memory usage high.*",
        "conditions": [
          {
            "field": "message",
            "condition": "Memory usage high",
            "comparison": "contains"
          }
        ]
      },
      "examples": [
        {
          "log_entry": "Memory usage within normal limits.",
          "expected_behavior": "No action required, memory usage is normal."
        },
        {
          "log_entry": "Memory usage high on application node 'app-node-2'. Current usage 92%",
          "expected_behavior": "Flag anomaly, notify DevOps team for resource optimization."
        }
      ],
      "action": {
        "flag": true,
        "notification": "Email",
        "severity_threshold": "medium"
      }
    },
    {
      "description": "Reliability anomaly - Frequent database connection failures",
      "type": "anomaly",
      "category": "Reliability",
      "severity": "high",
      "log_source": "application",
      "log_type": "ERROR",
      "pattern": {
        "expression": ".*Failed to connect to database.*",
        "conditions": [
          {
            "field": "message",
            "condition": "Failed to connect to database",
            "comparison": "contains"
          }
        ]
      },
      "examples": [
        {
          "log_entry": "Database connection established successfully.",
          "expected_behavior": "No action required, database connection is stable."
        },
        {
          "log_entry": "Failed to connect to database. Retrying in 5 seconds",
          "expected_behavior": "Flag anomaly, notify database administrators for investigation."
        }
      ],
      "action": {
        "flag": true,
        "notification": "Webhook",
        "severity_threshold": "high"
      }
    },
    {
      "description": "Observability anomaly - High latency on API endpoint",
      "type": "anomaly",
      "category": "Observability",
      "severity": "medium",
      "log_source": "application",
      "log_type": "WARN",
      "pattern": {
        "expression": ".*High latency detected on API endpoint.*",
        "conditions": [
          {
            "field": "message",
            "condition": "High latency",
            "comparison": "contains"
          }
        ]
      },
      "examples": [
        {
          "log_entry": "API response time within acceptable limits.",
          "expected_behavior": "No action required, API performance is normal."
        },
        {
          "log_entry": "High latency detected on API endpoint '/api/products'. Investigating issue",
          "expected_behavior": "Flag anomaly, notify API team for performance tuning."
        }
      ],
      "action": {
        "flag": true,
        "notification": "Slack",
        "severity_threshold": "medium"
      }
    }
  ]
}
    """

