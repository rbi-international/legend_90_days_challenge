"""
Test Script for Day 01 - python_sniper_utils

This script validates the core utility functions:
- setup_logger
- log_time decorator
- memoize decorator
- color_log output
"""

import os
import sys

# Ensure src is in Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.abspath(os.path.join(current_dir, "..", "src"))
sys.path.append(src_path)

from utils.python_sniper_utils import setup_logger, log_time, memoize, color_log

# Initialize logger
logger = setup_logger()

# Test log_time decorator
@log_time
def slow_add(a, b):
    import time
    time.sleep(1)
    return a + b

# Test memoize decorator
@memoize
def square(n):
    return n * n

if __name__ == "__main__":
    color_log("🚀 Starting Day 01 utility tests...", level="info", logger=logger)


    result1 = slow_add(10, 5)
    color_log(f"Result of slow_add(10, 5): {result1}", level="success", logger=logger)

    result2 = square(6)
    color_log(f"Result of square(6): {result2}", level="info", logger=logger)

    result3 = square(6)  # Should be cached
    color_log(f"Result of square(6) again (cached): {result3}", level="info", logger=logger)

    color_log("✅ All tests completed successfully!", level="success", logger=logger)
    
    # 🔥 Force flush logs to file
    for handler in logger.handlers:
        handler.flush()
