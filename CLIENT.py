import pickle
import socket

HOST = (socket.gethostname(), 9999)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем связку ip и порт
client.connect(HOST)

print("Connect...", HOST)

message = ""
# while True:
#     data = client.recv(8)
#     message += data.decode("UTF-8")
#     if not len(data):
#         break
# print(message)
# while True:
#     data = client.recv(8)
#     if len(data) == 0:
#         break
#     message += data.decode("UTF-8")
#     print(message)

# data = b""
# while True:
#     x = client.recv(1024)
#     data += x
#     if len(x) == 0:
#         break
#
# print(pickle.loads(data))

# requests = b"GET123 / HTTP/1.1\r\nHost:localhost:9999\r\n\r\n"
# requests = b"eeddfdf"
with open("1.jpg", "rb") as f:
    requests = f.read()
print(requests)


client.sendall(requests)
print("send msg")

