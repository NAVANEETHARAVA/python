def is_composite(n):
    if n <= 1:
        return False
    elif n <= 3:
        return False
    elif n % 2 == 0 or n % 3 == 0:
        return True
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return True
        i += 6
    return False

# Test the function
number = 15
if is_composite(number):
    print(number, "is a composite number")
else:
    print(number, "is not a composite number")
