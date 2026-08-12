# Function to ask user for input and return a list of computer statuses
def check_computers():
    computers = []  # Start with an empty list

    # Loop 5 times for 5 computers
    for i in range(1, 6):
        # Get input for each computer and convert to uppercase
        status = input(f"Computer {i} Status (A/U/M): ").upper()
        # Add the input status into the list
        computers.append(status)

    return computers  # Send the full list back