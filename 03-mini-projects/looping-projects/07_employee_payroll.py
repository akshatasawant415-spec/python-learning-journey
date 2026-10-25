number_of_employees = int(input("Enter number of employees: "))
if number_of_employees <= 0:
    print("Invalid number of employees")
    exit()
total_net_payroll = 0
for i in range(number_of_employees):
    name=input("Enter name of employee :")
    basic_salary=float(input("Enter salary :"))
    overtime_hours=int(input("Enter overtime hours :"))
    overtime_pay=overtime_hours*200
    gross_salary=basic_salary+overtime_pay
    if gross_salary>=50000:
        deduction_rate=10
    else:
        deduction_rate=5
    deduction_amount=gross_salary * deduction_rate /100
    net_salary=gross_salary-deduction_amount
    total_net_payroll = total_net_payroll + net_salary 
    print("Employee name :",name)
    print("gross salary :",gross_salary)
    print("salary :",basic_salary)
    print("deduction amount :",deduction_amount)
    print("net salary :",net_salary)
print("Total net payroll:", total_net_payroll)
print("Number of employees:", number_of_employees)  