"""
Day 01 - Smart Python Utilities

Custom tools for logging, performance measurement, and output formatting.
"""

import time
import logging
import functools
from datetime import datetime
import os

def setup_logger(name='legendary_logger', log_file=None, level=logging.INFO):
    """
    Sets up a logger that logs messages to both console and a file.
    Ensures absolute path logging regardless of where the script is run.
    """
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    logs_dir = os.path.join(base_dir, 'logs')
    os.makedirs(logs_dir, exist_ok=True)

    if log_file is None:
        log_file = os.path.join(logs_dir, 'legendary_log.log')

    formatter = logging.Formatter('%(asctime)s — %(levelname)s — %(message)s')

    file_handler = logging.FileHandler(log_file, mode='a', encoding='utf-8')
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers during reruns
    if not any(isinstance(h, logging.FileHandler) for h in logger.handlers):
        logger.addHandler(file_handler)
    if not any(isinstance(h, logging.StreamHandler) for h in logger.handlers):
        logger.addHandler(console_handler)

    return logger


def log_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        print(f"⏱️ {func.__name__} executed in {duration:.4f}s")
        return result
    return wrapper


def memoize(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"🧠 Cached result for {args}")
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper


def color_log(message, level="info", logger=None):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    color_codes = {
        "info": "\033[94m",
        "warning": "\033[93m",
        "error": "\033[91m",
        "success": "\033[92m",
        "endc": "\033[0m",
    }
    formatted = f"{color_codes.get(level, '')}[{timestamp}] {message}{color_codes['endc']}"
    print(formatted)

    # Also log to file if logger is passed
    if logger:
        if level == "success":
            logger.info(f"[SUCCESS] {message}")
        elif level == "error":
            logger.error(message)
        elif level == "warning":
            logger.warning(message)
        else:
            logger.info(message)

