fname = input("Enter the file name: ")

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
    sppos1 = line.find(" ")
    sppos2 = line.find(" ", sppos1 + 1)
    confidence = float(line[sppos1 + 1 : sppos2])
    total = total + confidence
    count = count + 1

print("Average spam confidence:", total / count)
