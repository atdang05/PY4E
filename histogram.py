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
    counts[words[1]] = counts.get(words[1], 0) + 1  # words[1] is email address

commits = [(count, email) for email, count in counts.items()]
commits.sort(reverse=True)
print(commits[0][1], commits[0][0])
