total = 0
count = 0

while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        num = int(num)
    except:
        print("Invalid input")
        continue

    total = total + num
    count = count + 1

print(total, count, total / count)
