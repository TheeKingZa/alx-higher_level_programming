
#!/usr/bin/python3

# Import necessary modules
import sys
from calculator_1 import add, sub, mul, div

# Check if the script is being run directly
if __name__ == "__main__":
    # Check if the number of command-line arguments is not 3
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Convert command-line arguments to integers
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    # Perform the operation based on the given operator
    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)
    else:
        # Print error message for unknown operator and exit
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Print the result in the specified format
    print(f"{a} {operator} {b} = {result}")

