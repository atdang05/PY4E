fname = input("Enter a file name: ")

try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

for line in fhand:
    line = line.rstrip().upper()
    print(line)
