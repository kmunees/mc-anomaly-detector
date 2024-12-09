# mc-anomaly-detector
# File Watcher and Vector Database Persistence

This Python project monitors file changes in a specified folder and persists the changes to a vector database. It provides an automated mechanism to track modifications, additions, or deletions in files and store relevant information (e.g., content, metadata) in a vector database for further processing, querying, or analysis.

## Functionality

- **File Watching**: The script continuously monitors a specified folder for any changes (file modifications, additions, deletions).
- **Vector Database Integration**: The changes detected are persisted to a vector database, where the content is stored as vectors for efficient searching and analysis.
- **Change Detection**: The program supports detecting new file additions
- **Logging**: All events (file changes, errors, etc.) are logged for monitoring and debugging purposes.

## Setup

### Prerequisites

Ensure you have the following installed on your machine:

- Python 3.12
- Required Python libraries (listed below)

### Installation Steps

1. **Clone the Repository**:  
   `git clone https://github.com/Matrix-Cloud-io/mc-anomaly-detector`  
   `cd mc-anomaly-detector`

2. **Create a Virtual Environment (Optional but recommended)**:  
   `python -m venv venv`  
   `source venv/bin/activate  # On Windows, use venv\Scripts\activate`

3. **Install Required Dependencies**:  
   `poetry install`

4. **Set Up Vector Database**:  
   - Configure the vector database based the `.env`
   - Add the required API keys or credentials to a `.env` file (or environment variables).

## Running the Project

### 1. Configure the Folder


### 2. Run the Script

To start monitoring the folder and persist changes to the vector database:  
`python main.py`

The script will now monitor the folder for any changes. When changes occur, the file content will be processed and persisted into the vector database.

### 3. Stopping the Script

To stop the file watcher, simply press `Ctrl+C` in the terminal.


