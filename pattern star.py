def right_angle_triangle(rows):
    for i in range(1, rows + 1):
        print("*" * i)

def inverted_right_angle_triangle(rows):
    for i in range(rows, 0, -1):
        print("*" * i)

def equilateral_triangle(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

def diamond(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

# Test the functions
rows = int(input("Enter the number of rows: "))

print("\nRight-angled Triangle Star Pattern:")
right_angle_triangle(rows)

print("\nInverted Right-angled Triangle Star Pattern:")
inverted_right_angle_triangle(rows)

print("\nEquilateral Triangle Star Pattern:")
equilateral_triangle(rows)

print("\nDiamond Star Pattern:")
diamond(rows)
