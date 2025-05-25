import socket
import os
from crypto_utils import load_key, decrypt_message, encrypt_message

# Check if the encryption key exists
if not os.path.exists("secret.key"):
    print("❌ Missing encryption key. Please run generate_key() first.")
    exit()

key = load_key()

server = socket.socket()
server.bind(('localhost', 9999))
server.listen(1)
print("✅ Server is listening on port 9999...")

conn, addr = server.accept()
print(f"🔌 Connected by {addr}")

try:
    while True:
        encrypted_msg = conn.recv(1024)
        if not encrypted_msg:
            print("⚠️ Client disconnected.")
            break
        decrypted_msg = decrypt_message(encrypted_msg, key)
        print("Client:", decrypted_msg)

        reply = input("You: ")
        conn.send(encrypt_message(reply, key))

except (ConnectionResetError, BrokenPipeError):
    print("⚠️ Connection lost. Client may have disconnected.")

finally:
    conn.close()
    server.close()
    print("🔒 Server connection closed.")
