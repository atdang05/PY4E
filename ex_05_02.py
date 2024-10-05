max = None
min = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        num = int(num)
    except:
        print("Invalid input")
        continue

    if max == None or max < num:
        max = num
    if min == None or min > num:
        min = num

print(max, min)
