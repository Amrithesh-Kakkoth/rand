#!/usr/bin/env python3
"""
Demo code file for testing the enhanced interactive CLI.
Contains various code quality issues for demonstration.
"""

import os
import requests

# Security issues
password = "admin123"  # Hardcoded password
api_key = "sk-1234567890abcdef"  # Hardcoded API key

def vulnerable_function(user_input):
    """Function with SQL injection vulnerability."""
    query = f"SELECT * FROM users WHERE name = '{user_input}'"
    return query

def dangerous_function(code_string):
    """Function using eval - security risk."""
    result = eval(code_string)
    return result

# Performance issues
def inefficient_loop(data_list):
    """Function with inefficient loop patterns."""
    result = ""
    for i in range(len(data_list)):
        result += str(data_list[i])
    return result

# Complexity issues
def complex_function(param1, param2, param3, param4, param5, param6, param7, param8):
    """Function with too many parameters."""
    if param1 > 0:
        if param2 > 0:
            if param3 > 0:
                if param4 > 0:
                    if param5 > 0:
                        if param6 > 0:
                            if param7 > 0:
                                if param8 > 0:
                                    return param1 + param2 + param3 + param4 + param5 + param6 + param7 + param8
    return 0

# Documentation issues
def undocumented_function(x, y):
    # Missing docstring
    return x + y

class UndocumentedClass:
    # Missing class docstring
    def __init__(self):
        self.value = 0
    
    def method_without_docstring(self):
        # Missing method docstring
        return self.value * 2

if __name__ == "__main__":
    print("Demo code for testing Code Quality Intelligence Agent")
