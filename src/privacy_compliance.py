```python
# src/privacy_compliance.py

from src.data_encryption import encrypt_data

class PrivacyCompliance:
    def __init__(self):
        self.user_consent = False

    def request_user_consent(self):
        # Request user consent for data processing
        # This is a placeholder, replace with actual implementation
        self.user_consent = True

    def check_user_consent(self):
        # Check if user has given consent
        return self.user_consent

    def process_data(self, data):
        # Process data only if user has given consent
        if self.check_user_consent():
            encrypted_data = encrypt_data(data)
            return encrypted_data
        else:
            raise Exception("User consent not given for data processing")

    def delete_data(self, data):
        # Delete data if user withdraws consent
        if not self.check_user_consent():
            # This is a placeholder, replace with actual implementation
            pass
        else:
            raise Exception("User consent not withdrawn, cannot delete data")
```