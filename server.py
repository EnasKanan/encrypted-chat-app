import socket
from crypto_utils import load_key, decrypt_message, encrypt_message

key = load_key()

server = socket.socket()
server.bind(('localhost', 9999))
server.listen(1)
print("Server listening...")

conn, addr = server.accept()
print("Connected by", addr)

while True:
    encrypted_msg = conn.recv(1024)
    if not encrypted_msg:
        break
    decrypted_msg = decrypt_message(encrypted_msg, key)
    print("Client:", decrypted_msg)

    reply = input("You: ")
    conn.send(encrypt_message(reply, key))