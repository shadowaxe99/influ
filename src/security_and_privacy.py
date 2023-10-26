```python
from cryptography.fernet import Fernet
import os

class DataEncryption:

    def __init__(self):
        self.key = os.environ.get('ENCRYPTION_KEY')
        self.cipher_suite = Fernet(self.key)

    def encrypt_data(self, data):
        encoded_data = data.encode('utf-8')
        encrypted_data = self.cipher_suite.encrypt(encoded_data)
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        decrypted_data = self.cipher_suite.decrypt(encrypted_data)
        return decrypted_data.decode('utf-8')


class PrivacyCompliance:

    def __init__(self, user_consent):
        self.user_consent = user_consent

    def check_user_consent(self):
        if not self.user_consent:
            raise Exception("User consent not provided. Cannot proceed with data processing.")
        return True
```