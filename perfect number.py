def is_perfect_number(num):
    if num <= 0:
        return False

    divisor_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i

    return divisor_sum == num

# Test the function
number = int(input("Enter a number to check if it's perfect: "))
if is_perfect_number(number):
    print(number, "is a perfect number.")
else:
    print(number, "is not a perfect number.")
