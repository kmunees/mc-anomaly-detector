from mod.env_loader import get_pgsql_db, get_pgsql_password, get_pgsql_host, get_pgsql_port, get_pgsql_user
import psycopg2
from mod.logger_configuration import logger

#Get logger
logger = logger()

db_config = {
    'dbname': f'{get_pgsql_db()}',
    'user': f'{get_pgsql_user()}',
    'password': f'{get_pgsql_password()}',
    'host': f'{get_pgsql_host()}',
    'port': get_pgsql_port()
}

def insert_processed_file_path(new_file):
    try:
        with psycopg2.connect(**db_config) as conn:
            with conn.cursor() as cursor:
                # Insert the new processed file
                cursor.execute("INSERT INTO public.mc_files (processed_files) VALUES (%s)", (new_file,))
                print("Processed file updated successfully.")
    except psycopg2.Error as e:
        print(f"Database error: {e}")

def is_file_processed(file_path):
    try:
        with psycopg2.connect(**db_config) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT 1 FROM public.mc_files WHERE processed_files = %s", (file_path,))
                result = cursor.fetchone()
                return result is not None
    except psycopg2.Error as e:
        print(f"Database error: {e}")
        return False

def get_patterns_from_db():
    try:
        # Connect to the database
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        # Query to fetch patterns
        query = """
        SELECT 
            id, description, "type", category, severity, log_source, log_type, 
            pattern_expression, pattern_conditions::jsonb, examples::jsonb, 
            action_flag, action_notification, action_severity_threshold 
        FROM public.mc_patterns;
        """
        cursor.execute(query)
        records = cursor.fetchall()
        # Transform the records into a list of dictionaries
        patterns = []
        for record in records:
            patterns.append({
                "id": record[0],
                "description": record[1],
                "type": record[2],
                "category": record[3],
                "severity": record[4],
                "log_source": record[5],
                "log_type": record[6],
                "pattern_expression": record[7],
                "pattern_conditions": record[8],
                "examples": record[9],
                "action_flag": record[10],
                "action_notification": record[11],
                "action_severity_threshold": record[12],
            })

        cursor.close()
        conn.close()
        return patterns

    except Exception as e:
        logger.error(f"Error fetching patterns from database: {str(e)}")
        return []
