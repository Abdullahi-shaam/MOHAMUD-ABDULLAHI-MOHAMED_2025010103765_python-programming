from student import get_student
from access import check_access, get_reason
from display import print_result


def main():
    name, student_id, registered, lab_open, computer = get_student()

    access = check_access(registered, lab_open, computer)

    if access:
        status = "Access Granted"
    else:
        status = "Access Denied"

    reason = get_reason(registered, lab_open, computer)

    print_result(name, student_id, status, reason)


main()