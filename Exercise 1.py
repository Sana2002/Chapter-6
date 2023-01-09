# Set a flag to indicate when to stop the loop
stop = False

# Create a list to store the toppings
toppings = []

# Start the loop
while not stop:
    # Prompt the user to enter a topping
    topping = input("Enter a topping for your pizza (or 'quit' to stop): ")

    # If the user enters 'quit', set the stop flag to True to exit the loop
    if topping == 'quit':
        stop = True
    # If the user does not enter 'quit', add the topping to the toppings list and print a message
    else:
        toppings.append(topping)
        print("We'll add " + topping + " to your pizza!")

# Print a summary of the toppings
print("\nYour pizza will have the following toppings:")
for topping in toppings:
    print(topping)
