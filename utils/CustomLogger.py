import logging
import os


def get_logger(name):
    # Get the project root directory (parent of utils directory)
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_dir = os.path.join(project_root, "logs")
    
    # Create logs directory if it doesn't exist
    os.makedirs(log_dir, exist_ok=True)
    
    log_file = os.path.join(log_dir, "orangehrm_logs.log")
    
    logging.basicConfig(filename=log_file,
                        format="%(asctime)s: %(levelname)s: %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.DEBUG, force=True)
    logger= logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger
