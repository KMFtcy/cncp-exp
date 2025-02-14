from loguru import logger
import sys

def setup_logger(config):
    """
    Configure logging using loguru
    
    Features:
    - Log rotation
    - JSON format output
    - Colored console output
    - Configurable log levels
    """
    # Get logging config section with defaults
    log_config = config.get('logging', {})
    log_level = log_config.get('level', 'INFO').upper()
    log_file = log_config.get('file', 'app.log')
    max_bytes = log_config.get('max_bytes', 10 * 1024 * 1024)  # Default 10MB
    backup_count = log_config.get('backup_count', 5)
    
    # Remove default handlers
    logger.remove()
    
    # Add console handler
    logger.add(
        sys.stdout,
        level=log_level,
        format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        colorize=True
    )
    
    # Add file handler
    logger.add(
        log_file,
        level=log_level,
        format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{function}:{line} - {message}",
        rotation=f"{max_bytes} B",  # Rotate when file reaches size limit
        retention=backup_count,     # Number of old files to keep
        compression="zip",          # Compress old log files
        serialize=True,             # Enable JSON format
        enqueue=True               # Thread-safe asynchronous writing
    )
    
    logger.info("Logger initialization completed with config: {}", {
        'level': log_level,
        'file': log_file,
        'max_bytes': max_bytes,
        'backup_count': backup_count
    })
