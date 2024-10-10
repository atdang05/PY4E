fname = input("Enter a file name: ")

try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

counts = dict()

for line in fhand:
    for char in line:
        if not char.isalpha():
            continue
        char = char.lower()
        counts[char] = counts.get(char, 0) + 1

lst = list()

for key, val in counts.items():
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst:
    print(val, key)
