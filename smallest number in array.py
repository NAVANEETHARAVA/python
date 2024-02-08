def find_smallest(arr):
    if not arr:
        return None  
    smallest = arr[0]  
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest

# Test the function
array = [5, 3, 9, 1, 7, 2]
smallest_number = find_smallest(array)
print("The smallest number in the array is:", smallest_number)
