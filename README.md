# Encrypted Chat Application 🔐💬

This project demonstrates a simple encrypted chat system using Python and AES encryption via the `cryptography` library.

## Features
- Peer-to-peer encrypted messaging
- AES key stored securely
- Uses socket programming for communication

## How to Use
1. Install dependencies:
   ```bash
   pip install cryptography
   ```
2. Generate a key (run once):
   ```python
   from crypto_utils import generate_key
   generate_key()
   ```
3. Start server:
   ```bash
   python server.py
   ```
4. Start client in another terminal:
   ```bash
   python client.py
   ```

## Ethical Use
This project is for educational use only. Do not use it to evade monitoring in unauthorized environments.