hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
if hours <= 40:
    pay = hours * rate
else:
    pay = 40 * rate + (hours - 40) * rate * 1.5
print("Pay:", pay)
