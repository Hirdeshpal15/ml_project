import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)


''' 
# To test --> python src/logger.py

if __name__=="__main__":
    logging.info("Logging has started")
    
'''


# LOG_FILE    --> will create log file with date
# logs_path   --> this will create .log file inside LOG_FILE
# os.getcwd   --> get current working directory, "Logs" --> naming convention
# os.makedirs --> make a directory
# logging.basicConfig --> this will add data in this format 
                        # (ex: [ 2026-02-19 19:24:12,605 ] 20 root - INFO - Logging has started)
