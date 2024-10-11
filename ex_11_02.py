import re

fname = input("Enter file: ")

try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

nums = list()

for line in fhand:
    nums += [int(num) for num in re.findall("^N.+: ([0-9]+)", line)]

print(int(sum(nums) / len(nums)))
