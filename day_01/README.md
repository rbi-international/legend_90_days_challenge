# 🧠 Day 01 - Smart Python Setup

Welcome to **Day 01** of your Legendary AI 90-Day Challenge!  
This day focused on setting up a modular Python utility system for scalable AI coding.

---

## 🎯 Objectives:
- ✅ Build a robust logger with both console & file output
- ✅ Create reusable decorators (`@log_time`, `@memoize`)
- ✅ Enable colored terminal logging
- ✅ Write a test script to validate all utilities
- ✅ Create an interactive walkthrough notebook

---

## 📂 Folder Structure:
```
day_01/
├── logs/ # File-based logs written here
├── notebooks/
│ └── day01_walkthrough.ipynb # Interactive explanation and demo
├── src/
│ ├── init.py
│ └── utils/
│ ├── init.py
│ └── python_sniper_utils.py # Core utility functions
└── tests/
└── test_day01_utils.py # Test script for logging and decorators
```


---

## 🔧 Utility Functions:

### 🪵 `setup_logger()`
Logs to terminal **and** writes to `logs/legendary_log.log` using a consistent format.

### ⏱️ `@log_time`
Decorator to time any function. Great for performance debugging.

### 🧠 `@memoize`
Caches outputs of pure functions to save time on repeated calls.

### 🎨 `color_log()`
Prints terminal messages with colors and timestamps (also integrated into logger).

---

## 📓 Notebook
Explore everything interactively in:  
`day01_walkthrough.ipynb`

---

## ✅ Learnings:
- Modular Python architecture for AI workflows
- Logging best practices with buffering and handlers
- Building extensible utility functions for large projects

---

## 🔗 Resources:
- [Logging Docs (Python)](https://docs.python.org/3/library/logging.html)
- [Python Decorators](https://realpython.com/primer-on-python-decorators/)

You're now geared up with a strong Python foundation for AI systems. On to Day 02!
