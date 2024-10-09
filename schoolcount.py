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
    mail = words[1].split("@")
    domain = mail[1]
    counts[domain] = counts.get(domain, 0) + 1

print(counts)
