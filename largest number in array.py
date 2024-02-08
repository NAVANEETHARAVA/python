def find_largest(arr):
    if not arr:
        return None  # Return None if array is empty
    largest = arr[0]  # Initialize largest to the first element of the array
    for num in arr:
        if num > largest:
            largest = num
    return largest

# Test the function
array = [5, 3, 9, 1, 7, 2]
largest_number = find_largest(array)
print("The largest number in the array is:", largest_number)
