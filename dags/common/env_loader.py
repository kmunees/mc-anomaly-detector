import os
from dotenv import load_dotenv

def load_environment_variables():
    """
    Load the environment variables from the appropriate .env file.
    """
    os.environ["ENV"] = "local"

    # Get the environment type (defaults to 'development' if not set)
    env = os.getenv('ENV', 'development')

    # Create the dotenv file name based on the environment
    dotenv_file = f".env.{env}"

    # Build the path to the correct .env file (two levels up from the current directory)
    dotenv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '../dags/env', dotenv_file)

    # Load the .env file
    load_dotenv(dotenv_path)

def get_milvus_host():
    """
    Get the MILVUS_PORT environment variable after loading the .env file.
    """
    # Ensure the environment variables are loaded first
    load_environment_variables()
    return os.getenv('MILVUS_HOST')

def get_milvus_port():
    """
    Get the MILVUS_PORT environment variable after loading the .env file.
    """
    # Ensure the environment variables are loaded first
    load_environment_variables()
    return os.getenv('MILVUS_PORT')

def get_milvus_url():
    """
    Get the MILVUS_PORT environment variable after loading the .env file.
    """
    # Ensure the environment variables are loaded first
    load_environment_variables()
    return os.getenv('MILVUS_URL')

def get_logfile_path():
    """
    Get the MILVUS_HOST environment variable after loading the .env file.
    """
    # Ensure the environment variables are loaded first
    load_environment_variables()
    return os.getenv('LOGFILE_PATH')

def get_pattern_file_path():
    """
    Get the MILVUS_HOST environment variable after loading the .env file.
    """
    # Ensure the environment variables are loaded first
    load_environment_variables()
    return os.getenv('PATTERN_FILE_PATH')

def get_api_key():
    """
    Get the API_VERSION environment variable after loading the .env file.
    """
    # Ensure the environment variables are loaded first
    load_environment_variables()
    return os.getenv('API_KEY')

def get_llm_model_url():
    """
    Get the AZURE_ENDPOINT environment variable after loading the .env file.
    """
    # Ensure the environment variables are loaded first
    load_environment_variables()
    return os.getenv('AZURE_ENDPOINT')

def get_model_api_version():
    """
    Get the API_VERSION environment variable after loading the .env file.
    """
    # Ensure the environment variables are loaded first
    load_environment_variables()
    return os.getenv('API_VERSION')