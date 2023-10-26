```python
from cryptography.fernet import Fernet

class DataEncryption:

    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def encrypt_data(self, data):
        encoded_data = data.encode('utf-8')
        encrypted_data = self.cipher_suite.encrypt(encoded_data)
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        decrypted_data = self.cipher_suite.decrypt(encrypted_data)
        return decrypted_data.decode('utf-8')
```