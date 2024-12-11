# delete from public.mc_files 
# 
# select * from public.mc_files 
# 
# CREATE TABLE public.mc_files (
#     id SERIAL PRIMARY KEY,                  -- Auto-generated id
#     org_id INTEGER ,                -- Organization ID
#     processed_files VARCHAR,                -- Processed files, could be an array or simple text
#     created_date TIMESTAMP DEFAULT NOW()    -- Timestamp for creation, default is current timestamp
# );


# CREATE TABLE public.mc_patterns (
#     id SERIAL PRIMARY KEY,
#     description TEXT NOT NULL,
#     type VARCHAR(50) NOT NULL,
#     category VARCHAR(50) NOT NULL,
#     severity VARCHAR(20) NOT NULL,
#     log_source VARCHAR(50) NOT NULL,
#     log_type VARCHAR(20) NOT NULL,
#     pattern_expression TEXT NOT NULL,
#     pattern_conditions JSONB NOT NULL, -- To store conditions array as JSON
#     examples JSONB NOT NULL,          -- To store example log entries as JSON
#     action_flag BOOLEAN NOT NULL,
#     action_notification VARCHAR(50) NOT NULL,
#     action_severity_threshold VARCHAR(20) NOT NULL
# );

#
# INSERT INTO public.mc_patterns (
#     description, score, type, category, severity, log_source, log_type,
#     pattern_expression, pattern_conditions, examples,
#     action_flag, action_notification, action_severity_threshold
# ) VALUES
# (
#     'Availability anomaly - Service outage detected',
#     85, -- Random score
#     'anomaly',
#     'Availability',
#     'high',
#     'application',
#     'WARN',
#     '.*service outage detected.*',
#     '[{"field": "message", "condition": "service outage", "comparison": "contains"}]',
#     '[{"log_entry": "All services are running normally. No errors detected at this time", "expected_behavior": "No action required, services are operational."},
#       {"log_entry": "Temporary service outage detected for ''EmailService''. Investigating further", "expected_behavior": "Flag anomaly, notify operations team for immediate investigation."}]',
#     TRUE,
#     'Email',
#     'high'
# ),
# (
#     'Security anomaly - Unauthorized access attempt',
#     62, -- Random score
#     'anomaly',
#     'Security',
#     'medium',
#     'application',
#     'ERROR',
#     '.*AccessDeniedException.*',
#     '[{"field": "message", "condition": "AccessDeniedException", "comparison": "contains"}]',
#     '[{"log_entry": "User login successful for username ''dave'' from IP 198.51.100.25", "expected_behavior": "No action required, user login is legitimate."},
#       {"log_entry": "AccessDeniedException: Unauthorized access attempt detected for sensitive endpoint", "expected_behavior": "Flag anomaly, notify security team."}]',
#     TRUE,
#     'Slack',
#     'medium'
# ),
# (
#     'Cost Efficiency anomaly - High memory usage',
#     47, -- Random score
#     'anomaly',
#     'Cost Efficiency',
#     'medium',
#     'infrastructure',
#     'WARN',
#     '.*Memory usage high.*',
#     '[{"field": "message", "condition": "Memory usage high", "comparison": "contains"}]',
#     '[{"log_entry": "Memory usage within normal limits.", "expected_behavior": "No action required, memory usage is normal."},
#       {"log_entry": "Memory usage high on application node ''app-node-2''. Current usage 92%", "expected_behavior": "Flag anomaly, notify DevOps team for resource optimization."}]',
#     TRUE,
#     'Email',
#     'medium'
# ),
# (
#     'Reliability anomaly - Frequent database connection failures',
#     93, -- Random score
#     'anomaly',
#     'Reliability',
#     'high',
#     'application',
#     'ERROR',
#     '.*Failed to connect to database.*',
#     '[{"field": "message", "condition": "Failed to connect to database", "comparison": "contains"}]',
#     '[{"log_entry": "Database connection established successfully.", "expected_behavior": "No action required, database connection is stable."},
#       {"log_entry": "Failed to connect to database. Retrying in 5 seconds", "expected_behavior": "Flag anomaly, notify database administrators for investigation."}]',
#     TRUE,
#     'Webhook',
#     'high'
# ),
# (
#     'Observability anomaly - High latency on API endpoint',
#     74, -- Random score
#     'anomaly',
#     'Observability',
#     'medium',
#     'application',
#     'WARN',
#     '.*High latency detected on API endpoint.*',
#     '[{"field": "message", "condition": "High latency", "comparison": "contains"}]',
#     '[{"log_entry": "API response time within acceptable limits.", "expected_behavior": "No action required, API performance is normal."},
#       {"log_entry": "High latency detected on API endpoint ''/api/products''. Investigating issue", "expected_behavior": "Flag anomaly, notify API team for performance tuning."}]',
#     TRUE,
#     'Slack',
#     'medium'
# );


import psycopg2

def insert_processed_file_path(new_file):
    db_config = {
        'dbname': 'airflow',
        'user': 'airflow',
        'password': 'airflow',
        'host': '192.168.29.111',
        'port': 5432
    }
    try:
        with psycopg2.connect(**db_config) as conn:
            with conn.cursor() as cursor:
                # Insert the new processed file
                cursor.execute("INSERT INTO public.mc_files (processed_files) VALUES (%s)", (new_file,))
                print("Processed file updated successfully.")
    except psycopg2.Error as e:
        print(f"Database error: {e}")

def is_file_processed(file_path):
    db_config = {
        'dbname': 'airflow',
        'user': 'airflow',
        'password': 'airflow',
        'host': '192.168.29.111',
        'port': 5432
    }
    try:
        with psycopg2.connect(**db_config) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT 1 FROM public.mc_files WHERE processed_files = %s", (file_path,))
                result = cursor.fetchone()
                return result is not None
    except psycopg2.Error as e:
        print(f"Database error: {e}")
        return False