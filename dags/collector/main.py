# from mc.collector.log_file_reader import detect_anomaly
# from mc.config.logger_configuration import logger
# from mc.config.llm_configuration import initialize_models
# from flask import Flask
# import threading
# from mc.report.report_controller import api_blueprint
# from mc.vector.milvus_client import create_milvus_collection
#
# app = Flask(__name__)
#
# # Get logger
# logger = logger()
#
# def run_flask():
#     initialize_models()
#     app.run(debug=True, use_reloader=False)
#
# def main():
#     logger.info("Application started - Listening for new log files in the specified directory.")
#     create_milvus_collection()
#     detect_anomaly()
#
# # Register the API blueprint with the app
# app.register_blueprint(api_blueprint, url_prefix='/api')
#
# if __name__ == "__main__":
#     flask_thread = threading.Thread(target=run_flask)
#     flask_thread.start()
#     main()
