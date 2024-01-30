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


def save_img(b):
    with open("2.jpg", "wb") as f:
        f.write(b)


while True:
    client, address = s.accept()
    print("connected - ", address)

    req = b''
    while True:
        data = client.recv(1024)
        if not len(data):
            break
        req += data
    save_img(req)
    client.close()

"""
Задача "Чат-сервер":
Реализуйте простой чат-сервер, который позволяет нескольким клиентам обмениваться сообщениями. 
Каждый клиент должен подключаться к серверу через сокет и отправлять сообщения, которые будут видны 
всем остальным клиентам.
"""

