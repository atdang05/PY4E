import urllib.request, urllib.parse, urllib.error

url = input("Enter URL: ")
fhand = urllib.request.urlopen(url)
count = 0

for line in fhand:
    if count + len(line) < 3000:
        print(line.decode(), end="")
    elif count < 3000:
        print(line[: 3000 - count].decode())
    count += len(line)

print(count)
