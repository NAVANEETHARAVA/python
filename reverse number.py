def reverse_number(number):
    reversed_number = 0
    while number > 0:
        remainder = number % 10
        reversed_number = (reversed_number * 10) + remainder
        number = number // 10
    return reversed_number

# Example usage
num = int(input("Enter a number: "))
reversed_num = reverse_number(num)
print("The reversed number:", reversed_num)
