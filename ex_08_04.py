fname = input("Enter file: ")

try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

lst = list()

for line in fhand:
    words = line.split()
    for word in words:
        if word in lst:
            continue
        lst.append(word)
    lst.sort()

print(lst)
