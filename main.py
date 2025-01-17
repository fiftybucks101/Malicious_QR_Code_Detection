from src.MaliciousQRCodeDetection.logging.logger import logger  
from src.MaliciousQRCodeDetection.exception import MaliciousQRException
import sys

def main():
    try:
        # Intentional ZeroDivisionError
        result = 1 / 0
    except Exception as e:
        logger.error('Zero division error occured')
        raise MaliciousQRException(e,sys)

if __name__ == "__main__":
    main()
