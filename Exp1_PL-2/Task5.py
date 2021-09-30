count = 1
while count <= 10:
        work_hrs = int(input("Enter the no. of working hours of Employees: "))
        if (work_hrs > 40):
            overtime = work_hrs - 40
            overtime_money = overtime * 12.00
            print("Employee number", count, "Overtime pay is ", overtime_money)
        else:
            print("You have to work more than 40 hours")
        count += 1

