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
import psycopg2

def insert_processed_file(new_file):
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