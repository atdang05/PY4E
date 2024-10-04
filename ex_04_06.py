def computepay(hours, rate):
    if hours <= 40:
        return hours * rate
    else:
        return 40 * rate + (hours - 40) * rate * 1.5


try:
    h = float(input("Enter Hours: "))
    r = float(input("Enter Rate: "))
except:
    print("Error, please enter numeric input")
    exit()
print("Pay:", computepay(h, r))
