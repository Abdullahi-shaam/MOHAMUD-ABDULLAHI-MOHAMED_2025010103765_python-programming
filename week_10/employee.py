def get_employee():
    print("=== Employee Information ===")
    
    name = input("Employee Name : ")
    employee_id = input("Employee ID   : ")
    basic_salary = float(input("Basic Salary (RM): "))
    allowance = float(input("Allowance (RM): "))
    
    # New Inquiry 2.1: Overtime hours worked
    overtime_hours = float(input("Overtime Hours Worked: "))
    
    # New Inquiry 2.2: Years of service for reward/bonus
    years_worked = float(input("Years of Service: "))
    
    return name, employee_id, basic_salary, allowance, overtime_hours, years_worked