import pickle
import socket

HOST = (socket.gethostname(), 9999)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем связку ip и порт
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # очистка порта для его переисользования

s.bind(HOST)
s.listen()
print("Cервер работает")

# while True:
#     client, address = s.accept()
#     print("connected - ", address)
#     res = b"Hello, from server"
#     client.send(res)
#     client.close()

user = {str(i): i for i in range(1000)}

# while True:
#     client, address = s.accept()
#     print("connected - ", address)
#     res = pickle.dumps(user)
#     client.send(res)
#     client.close()
"""
Задача "Передача файлов":
Напишите программу, которая позволяет клиенту загружать файлы на сервер через сокеты.
"""
while True:
    client, address = s.accept()
    print("connected - ", address)

    req = ''
    while True:
        data = client.recv(1024)
        if not len(data):
            break
        req += data.decode()
    print(req)
    client.close()

with open("path", "r") as f:
    s = f.read().encode("utf-8")