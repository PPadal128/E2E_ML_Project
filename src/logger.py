import logging
import os
from datetime import datetime



LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(), "logs")
os.makedirs(log_path, exist_ok=True)

log_file_path = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename=log_file_path,
    level=logging.DEBUG,
    format="[ %(asctime)s ] %(levelno)d - %(name)s - %(levelname)s - %(message)s"
)





# chaluchi ki nahi  checking/test pain lekhichi, but is not required in original code 
if __name__ == "__main__":
    logging.info("Logging has Started")
    logging.info("This is an info message")
    logging.debug("This is a debug message")
    logging.warning("This is a warning message")
    