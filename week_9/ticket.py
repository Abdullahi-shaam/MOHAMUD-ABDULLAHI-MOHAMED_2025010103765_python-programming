def create_ticket():

    print("=== IT Helpdesk Ticket ===")

    student_id = input("Student ID : ")
    student_name = input("Student Name : ")
    issue = input("Issue : ")
    location = input("Location : ")
    priority = input("Priority (High/Medium/Low): ")

    ticket = {
        "student_id": student_id,
        "student_name": student_name,
        "issue": issue,
        "location": location,
        "priority": priority,
        "status": "Pending"
    }

    return ticket