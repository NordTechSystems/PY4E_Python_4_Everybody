
def computePay(hours, rate):
    # print("In computePay", hours, rate)
    if hours > 40 :
        regular_pay = hours * rate
        overtime_pay = (hours - 40.0) * (rate * 0.5)
        # print(regular_pay,overtime_pay)
        hours_times_rate = regular_pay + overtime_pay
    else :
        hours_times_rate = hours * rate
    # print("Returning", hours_times_rate)
    return hours_times_rate

enter_hours = input("Enter Hours: ")
enter_rate = input("Enter Rate: ")
floatingPointHours = float(enter_hours)
floatingPointRate = float(enter_rate)
# print(floatingPointHours, floatingPointRate)
returnedPay = computePay(floatingPointHours, floatingPointRate)

print("Pay:",returnedPay)
