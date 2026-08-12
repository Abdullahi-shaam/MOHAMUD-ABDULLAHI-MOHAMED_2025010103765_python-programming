# Function to display the formatted lab status output
def display_status(computers, available):
    print("\n========== LAB STATUS ==========")

    # Loop through indices 0 to 4 to show computer number and status
    for number in range(len(computers)):
        print(f"Computer {number + 1}: {computers[number]}")

    print("------------------------------")
    print(f"Available Computers: {available}")
    print("==============================")