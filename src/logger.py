import logging
import os
from datetime import datetime

# اسم الملف بتاريخ ووقت
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

# فولدر logs
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# المسار الكامل للملف
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# إعدادات اللوج
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    level=logging.INFO,
    force=True
)

if __name__ == "__main__":
    logging.info("Logging has started")
    logging.warning("This is a warning")
    logging.error("This is an error")
