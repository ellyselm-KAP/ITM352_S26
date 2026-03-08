# Name: Ellyse McChesney
# Date: Jan 27, 2026  
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

encode_text = cipher_suite.encrypt(b"This is a really secret message.")
print(f"Encoded text: {encoded_text}")

# Use the cryptography libraary to encode and decode a essage 
decode_text = cipher_suite.decrypt(encoded_text)
print(f"Decoded text: (decoded_text.decode("utf.8)")


print(crypotgraphy.__version__)


user_message = input("Enter a message to encrypt: ")

# Encode string to bytes
message_bytes = user_message.encode("utf-8")

# Encrypt
encrypted = cipher.encrypt(message_bytes)
print(f"Encrypted message: {encrypted.decode('utf-8')}")

# Decrypt
decrypted = cipher.decrypt(encrypted)
print(f"Decrypted message: {decrypted.decode('utf-8')}")
