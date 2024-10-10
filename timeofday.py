fname = input("Enter a file name: ")

try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

counts = dict()

for line in fhand:
    if not line.startswith("From") or line.startswith("From:"):
        continue
    words = line.split()
    hour, minute, second = words[5].split(":")
    counts[hour] = counts.get(hour, 0) + 1

lst = list()

for key, val in counts.items():
    lst.append((key, val))

lst.sort()

for key, val in lst:
    print(key, val)
