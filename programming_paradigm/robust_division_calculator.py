# robust_division_calculator.py

print("robust_division_calculator.py is loaded")  # Debugging statement

def safe_divide(numerator, denominator):
    try:
        num = float(numerator)  # Convert numerator to float
        denom = float(denominator)  # Convert denominator to float
        
        result = num / denom  # Perform the division
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."
