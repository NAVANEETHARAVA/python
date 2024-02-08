import math

def square_root(num):
    if num < 0:
        return "Square root is not defined for negative numbers"
    else:
        return math.sqrt(num)

# Example usage
number = float(input("Enter a number: "))
result = square_root(number)
print("Square root of", number, "is:", result)
