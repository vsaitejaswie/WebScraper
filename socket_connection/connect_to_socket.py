import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('data.pr4e.org', 80))
print("success")
cmd = "GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n".encode()
#encode() is used to sent the request in UTF-8 format, python internally uses unicode
mysocket.send(cmd)
print("success")

while True:
    data = mysocket.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())

mysocket.close()