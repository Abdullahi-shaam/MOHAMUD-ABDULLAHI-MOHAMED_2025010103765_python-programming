from ticket import create_ticket
from display import display_ticket


def main():

    ticket = create_ticket()

    if ticket["priority"].lower() == "high":
        ticket["technician"] = "Ahmad"
    elif ticket["priority"].lower() == "medium":
        ticket["technician"] = "Siti"
    elif ticket["priority"].lower() == "low":
        ticket["technician"] = "Ali"
    else:
        ticket["technician"] = "Not Assigned"

    display_ticket(ticket)


if __name__ == "__main__":
    main()