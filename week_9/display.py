def display_ticket(ticket):

    print("\n======== HELPDESK TICKET ========")

    print("Student ID :", ticket["student_id"])
    print("Student    :", ticket["student_name"])
    print("Issue      :", ticket["issue"])
    print("Location   :", ticket["location"])
    print("Priority   :", ticket["priority"])
    print("Technician :", ticket["technician"])
    print("Status     :", ticket["status"])

    print("=================================")