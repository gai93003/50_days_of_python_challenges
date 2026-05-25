############### Extra Challenge: Teacher's Salary ###############

# A school has asked you to write a program that will calculate teachers' salaries. The program should ask the user to enter the teacher's name, the number of periods taught in a month, and the rate per period. The monthly salary is calculated by multiplying the number of periods by the monthly rate.

#The current monthy rate per period is $20. If a teacher has more than 100 periods in a month, every above 100 is overtime. Overtime is $25 period. For example, if a teacher has taught 105 periods, their monthly gross salary should by 2,125. 

# Write a function called "your_salary" that calculates the teacher's gross salary. The function should return the teacher's name, periods taught, and gross salary. Here is how you should format your output:

# Teacher: John Kelly,
# Periods: 105
# Gross salary; 2,125

def your_salary():
    name = input("Enter the teacher's name: ")
    periods = int(input("Enter the number of periods: "))
    normal_rate = 20
    overtime_rate = 25
    gross_salary = 0

    if periods > 100:
        extra_periods = periods - 100
        normal_pay = 100 * normal_rate
        extra_pay = extra_periods * overtime_rate

        gross_salary = normal_pay + extra_pay
    else:
        gross_salary = periods * normal_rate

    return f"\n Teacher: {name}\n Periods: {periods}\n Gross salary: {gross_salary}"

print(your_salary())