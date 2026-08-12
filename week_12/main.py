# Import the functions from the other Python files (modules)
from check import check_computers
from count import count_available
from display import display_status


def main():
    # Loop to keep monitoring until technician stops
    while True:
        # Get computer statuses from check module
        computers = check_computers()

        # Count available computers from count module
        available = count_available(computers)

        # Print report from display module
        display_status(computers, available)

        # Prompt user to continue or stop
        choice = (
            input("\nPerform another monitoring cycle? (Y/N): ")
            .strip()
            .upper()
        )

        # Stop loop if user types anything other than 'Y'
        if choice != "Y":
            print("Exiting monitoring system. Goodbye!")
            break


# Run the main program
if __name__ == "__main__":
    main()