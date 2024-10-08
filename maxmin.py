nums = list()

while True:
    inp = input("Enter a number: ")

    try:
        inp = float(inp)
    except:
        if inp == "done":
            break
        else:
            print("Invalid input")
            continue

    nums.append(inp)

print("Maximum:", max(nums))
print("Minimum:", min(nums))
