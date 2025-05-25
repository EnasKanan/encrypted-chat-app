import socket
import os
from crypto_utils import load_key, encrypt_message, decrypt_message

# Check if the encryption key exists
if not os.path.exists("secret.key"):
    print("❌ Missing encryption key. Please run generate_key() first.")
    exit()

key = load_key()

client = socket.socket()

try:
    client.connect(('localhost', 9999))
    print("✅ Connected to server.")

    while True:
        message = input("You: ")
        if not message:
            continue
        client.send(encrypt_message(message, key))

        encrypted_reply = client.recv(1024)
        if not encrypted_reply:
            print("⚠️ Server disconnected.")
            break
        print("Server:", decrypt_message(encrypted_reply, key))

except ConnectionRefusedError:
    print("❌ Unable to connect. Make sure the server is running.")

except (ConnectionResetError, BrokenPipeError):
    print("⚠️ Connection lost. Server may have disconnected.")

finally:
    client.close()
    print("🔒 Connection closed.")