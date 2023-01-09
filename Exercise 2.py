# Set a flag to indicate when to stop the loop
stop = False

# Start the loop
while not stop:
    # Prompt the user to enter their age
    age = input("Enter your age (or 'quit' to stop): ")

    # If the user enters 'quit', set the stop flag to True to exit the loop
    if age == 'quit':
        stop = True
    # If the user does not enter 'quit', determine the ticket price based on their age
    else:
        # Convert the age string to an integer
        age = int(age)

        # If the age is less than 3, the ticket is free
        if age < 3:
            price = 0
        # If the age is between 3 and 12, the ticket is $10
        elif age >= 3 and age <= 12:
            price = 10
        # If the age is over 12, the ticket is $15
        else:
            price = 15

        # Print the ticket price
        print("Your ticket will cost $" + str(price) + ".")
