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
    mail = words[1]
    counts[mail] = counts.get(mail, 0) + 1

lst = list()

for key, val in counts.items():
    lst.append((val, key))

lst.sort(reverse=True)
print(lst[0][1], lst[0][0])
