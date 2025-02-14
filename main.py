#!/usr/bin/env python3
import sys
from loguru import logger
# from src.network.socket_handler import SocketHandler
# from src.control.congestion_controller import CongestionController
from src.utils.config import read_config
from src.utils.logger import setup_logger

def main():
    try:
        # Load configuration first
        config = read_config()
        print(config)
        
        # Setup logging with configuration
        setup_logger(config)
        
        logger.info("Starting congestion control service...")
        
        # Initialize congestion controller
        # controller = CongestionController(config)
        
        # Initialize socket handler
        # socket_handler = SocketHandler(controller, config)
        
        # Start service
        # socket_handler.start()
        
    except KeyboardInterrupt:
        logger.info("Program is shutting down...")
        sys.exit(0)
    except Exception as e:
        # Use logger.exception to automatically capture the full traceback
        logger.exception("Program error: {}", str(e))
        sys.exit(1)

if __name__ == "__main__":
    main() 