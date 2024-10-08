fname = input("Enter file: ")

try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

out = list()

for line in fhand:
    words = line.split()

    for word in words:
        if word in out:
            continue

        out.append(word)

out.sort()
print(out)
