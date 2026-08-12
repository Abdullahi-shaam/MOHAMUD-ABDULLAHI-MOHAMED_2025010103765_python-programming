# Function to count how many "A" (Available) statuses are in the list
def count_available(computers):
    available = 0  # Initial counter set to 0

    # Look through every status in the list
    for status in computers:
        # Check if the status is "A"
        if status == "A":
            available += 1  # Add 1 to available count

    return available  # Return the final count