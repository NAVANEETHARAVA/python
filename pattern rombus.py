def rhombus_pattern(rows):
    for i in range(1, rows + 1):
        # Print leading spaces
        for j in range(rows - i):
            print(" ", end="")
        
        # Print stars
        for k in range(2 * i - 1):
            print("*", end="")
        
        print()
    
    for i in range(rows - 1, 0, -1):
        # Print leading spaces
        for j in range(rows - i):
            print(" ", end="")
        
        # Print stars
        for k in range(2 * i - 1):
            print("*", end="")
        
        print()

# Test the function
rows = int(input("Enter the number of rows: "))
rhombus_pattern(rows)
