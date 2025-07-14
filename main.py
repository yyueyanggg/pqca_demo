from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os

# This would be detected by CBOMkit
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"my secret message")