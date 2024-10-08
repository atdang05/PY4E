nums = list()

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        nums.append(float(num))
    except:
        print("Invalid input")
        continue

print("Maximum:", max(nums))
print("Minimum:", min(nums))
