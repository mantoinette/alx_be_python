# division_main.py

import sys
from robust_division_calculator import safe_divide  # Import the safe_divide function from robust_division_calculator.py

def main():
    if len(sys.argv) != 3:
        print("Usage: python division_main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
