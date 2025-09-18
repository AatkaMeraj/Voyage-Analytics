import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.flight_price_prediction import logger

if __name__ == "__main__":
    logger.info("✅ Demo script is running successfully!")