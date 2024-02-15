def calculate_simple_interest(principal, rate, time):
    # Simple Interest Formula: SI = P * R * T / 100
    simple_interest = (principal * rate * time) / 100
    return simple_interest

# Input principal amount, rate of interest, and time period from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in percentage): "))
time = float(input("Enter the time period (in years): "))

# Calculate simple interest
simple_interest = calculate_simple_interest(principal, rate, time)

# Print the result
print("The simple interest is:", simple_interest)
                    
