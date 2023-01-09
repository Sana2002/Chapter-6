# Create a list of sandwich orders
sandwich_orders = ['tuna', 'grilled cheese', 'chicken', 'francisco']

# Create an empty list to store finished sandwiches
finished_sandwiches = []

# Loop through the sandwich orders
for sandwich in sandwich_orders:
    # Print a message for the current sandwich
    print("I made your " + sandwich + " sandwich.")
    # Add the sandwich to the list of finished sandwiches
    finished_sandwiches.append(sandwich)

# Print a summary of the finished sandwiches
print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich)
