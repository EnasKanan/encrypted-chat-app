import socket
from crypto_utils import load_key, encrypt_message, decrypt_message

key = load_key()

client = socket.socket()
client.connect(('localhost', 9999))

while True:
    message = input("You: ")
    client.send(encrypt_message(message, key))

    encrypted_reply = client.recv(1024)
    print("Server:", decrypt_message(encrypted_reply, key))