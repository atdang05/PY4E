import socket

url = input("Enter URL: ")
host = url.split("/")[0]
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, 80))
cmd = f"GET http://{url} HTTP/1.0\r\n\r\n".encode()
mysock.send(cmd)
count = 0

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    if count + len(data) < 3000:
        print(data.decode(), end="")
    elif count < 3000:
        print(data[: 3000 - count].decode())
    count += len(data)

print(count)
mysock.close()
