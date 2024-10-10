fname = input("Enter a file name: ")

try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

counts = dict()

for line in fhand:
    line = line.lower()

    for letter in line:
        if not letter.isalpha():
            continue

        counts[letter] = counts.get(letter, 0) + 1

letters = [(count, letter) for letter, count in counts.items()]
letters.sort(reverse=True)

for item in letters:
    print(item[1], item[0])
