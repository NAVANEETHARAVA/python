def is_palindrome(input_str):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    input_str = input_str.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return input_str == input_str[::-1]

# Example usage
string = input("Enter a string or number: ")
if is_palindrome(string):
    print("Yes, it is a palindrome.")
else:
    print("No, it is not a palindrome.")
