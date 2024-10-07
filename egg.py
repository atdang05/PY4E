fname = input("Enter the file name: ")

if not fname == "na na boo boo":
    try:
        fhand = open(fname)
    except:
        print("File cannot be opened:", fname)
        exit()

    count = 0

    for line in fhand:
        if line.startswith("Subject:"):
            count = count + 1

    print(f"There were {count} subject lines in {fname}")
else:
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
