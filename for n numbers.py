def generate_numbers(n):
    numbers = []
    for i in range(1, n + 1):
        numbers.append(i)
    return numbers

# Test the function
n = int(input("Enter the number of numbers to generate: "))
result = generate_numbers(n)
print("Generated numbers:", result)
