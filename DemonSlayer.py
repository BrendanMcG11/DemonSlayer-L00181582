# DemonSlayer.py

import logging

# Basic logging configuration
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def add(a, b):
    """
    Function to add two numbers.
    Args:
    - a (int or float): The first number.
    - b (int or float): The second number.

    Returns:
    - sum (int or float): The sum of a and b.
    """
    logging.info(f"add() called with a={a}, b={b}")
    result = a + b
    logging.info(f"add() result: {result}")
    return result

def subtract(a, b):
    """
    Function to subtract the second number from the first number.
    Args:
    - a (int or float): The first number.
    - b (int or float): The second number to subtract from the first.

    Returns:
    - result (int or float): The result of a - b.
    """
    logging.info(f"subtract() called with a={a}, b={b}")
    result = a - b
    logging.info(f"subtract() result: {result}")
    return result
