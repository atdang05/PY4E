max = None
min = None

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

    if max == None or max < inp:
        max = inp

    if min == None or min > inp:
        min = inp

print(max, min)
