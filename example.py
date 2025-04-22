"""Example module demonstrating basic Python features.

This module contains example functions to demonstrate documentation generation.
"""

def greet(name: str) -> str:
    """Return a personalized greeting message.
    
    Args:
        name: The name of the person to greet
        
    Returns:
        A greeting message including the person's name
    """
    return f"Hello, {name}! Welcome to the tutorial."

def calculate_sum(numbers: list[int]) -> int:
    """Calculate the sum of a list of numbers.
    
    Args:
        numbers: List of integers to sum
        
    Returns:
        The sum of all numbers in the list
    """
    return sum(numbers)

class Calculator:
    """A simple calculator class demonstrating object-oriented programming.
    
    This class provides basic arithmetic operations.
    """
    
    def add(self, a: float, b: float) -> float:
        """Add two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The sum of a and b
        """
        return a + b
    
    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The product of a and b
        """
        return a * b 