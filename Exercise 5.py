# Create a list of sandwich orders
sandwich_orders = ['tuna', 'grilled cheese', 'Chicken', 'Francisco', 'pastrami', 'pastrami', 'pastrami']

# Print a message that pastrami has run out
print("Sorry, we're all out of pastrami.")

# Use a while loop to remove all occurrences of pastrami from the list
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Create an empty list to store finished sandwiches
finished_sandwiches = []

# Loop through the remaining sandwich orders
for sandwich in sandwich_orders:
    # Print a message for the current sandwich
    print("I made your " + sandwich + " sandwich.")
    # Add the sandwich to the list of finished sandwiches
    finished_sandwiches.append(sandwich)

# Print a summary of the finished sandwiches
print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich)
