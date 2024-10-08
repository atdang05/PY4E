fname = input("Enter a file name: ")

try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

count = 0
for line in fhand:
    if not line.startswith("From"):
        continue

    if line.startswith("From:"):
        continue

    words = line.split()
    print(words[1])
    count = count + 1

print(f"There were {count} lines in the file with From as the first word")
