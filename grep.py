import re

regex = input("Enter a regular expression: ")
fhand = open("mbox.txt")

count = 0

for line in fhand:
    if re.search(regex, line):
        count += 1

print(f"mbox.txt had {count} lines that matched {regex}")
