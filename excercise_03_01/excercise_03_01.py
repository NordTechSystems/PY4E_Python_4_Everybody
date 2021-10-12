enter_hours = input("Enter Hours: ")
enter_rate = input("Enter Rate: ")
floatingPointHours = float(enter_hours)
floatingPointRate = float(enter_rate)
# print(floatingPointHours, floatingPointRate)
if floatingPointHours > 40 :
    # print("Overtime")
    regular_pay = floatingPointHours * floatingPointRate
    overtime_pay = (floatingPointHours - 40.0) * (floatingPointRate * 0.5)
    # print(regular_pay,overtime_pay)
    hours_times_rate = regular_pay + overtime_pay
else :
    # print("Regular")
    regular_pay = floatingPointHours * floatingPointRate
    hours_times_rate = floatingPointHours * floatingPointRate
print("Pay:",hours_times_rate)
