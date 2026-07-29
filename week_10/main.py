from employee import get_employee
from salary import calculate_gross_salary, calculate_epf, calculate_socso, calculate_net_salary
from report import print_report

def main():
    # 1. Collect employee data
    name, employee_id, basic_salary, allowance, overtime_hours, years_worked = get_employee()
    
    # 2. Perform calculations
    gross_salary = calculate_gross_salary(basic_salary, allowance, overtime_hours, years_worked)
    epf = calculate_epf(gross_salary)
    socso = calculate_socso(gross_salary)
    net_salary = calculate_net_salary(gross_salary, epf, socso)
    
    # 3. Print the report
    print_report(name, employee_id, gross_salary, epf, socso, net_salary)

if __name__ == "__main__":
    main()