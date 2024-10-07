fname = input("Enter a file name: ")

try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

total = 0
count = 0

for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    colpos = line.find(":")
    num = float(line[colpos + 1 :])
    total = total + num
    count = count + 1

print("Average spam confidence:", total / count)
