total = 0
count = 0

while True:
    inp = input("Enter a number: ")

    try:
        inp = int(inp)
    except:
        if inp == "done":
            break
        else:
            print("Invalid input")
            continue

    count = count + 1
    total = total + inp

print(total, count, total / count)
