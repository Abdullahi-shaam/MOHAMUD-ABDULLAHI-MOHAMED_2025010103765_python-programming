def calculate_gross_salary(basic_salary, allowance, overtime_hours, years_worked):
    # New Inquiry 2.1: Overtime paid at RM25 per hour
    overtime_pay = overtime_hours * 25.0
    
    # New Inquiry 2.2: Reward for employees with > 3 years of service (e.g., RM500 bonus)
    bonus = 500.0 if years_worked > 3 else 0.0
    
    gross_salary = basic_salary + allowance + overtime_pay + bonus
    return gross_salary

def calculate_epf(gross_salary):
    # EPF deduction is 11%
    return gross_salary * 0.11

def calculate_socso(gross_salary):
    # SOCSO deduction is 0.5%
    return gross_salary * 0.005

def calculate_net_salary(gross_salary, epf, socso):
    return gross_salary - epf - socso