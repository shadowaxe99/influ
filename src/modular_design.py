```python
# src/modular_design.py

from src.sorting import sort_contacts
from src.user_interface import display_preview, load_profile, save_profile
from src.data_encryption import encrypt_data
from src.error_handling import handle_error
from src.integration import integrate_with_cms

class ComplexContactsSorting:
    def __init__(self, contact_list, sorting_criteria, sorting_profiles):
        self.contact_list = contact_list
        self.sorting_criteria = sorting_criteria
        self.sorting_profiles = sorting_profiles

    def sort_contacts(self):
        try:
            sorted_contacts = sort_contacts(self.contact_list, self.sorting_criteria)
            return sorted_contacts
        except Exception as e:
            handle_error(e)

    def display_preview(self):
        try:
            preview = display_preview(self.contact_list, self.sorting_criteria)
            return preview
        except Exception as e:
            handle_error(e)

    def save_profile(self, profile_name):
        try:
            save_profile(self.sorting_profiles, profile_name, self.sorting_criteria)
        except Exception as e:
            handle_error(e)

    def load_profile(self, profile_name):
        try:
            self.sorting_criteria = load_profile(self.sorting_profiles, profile_name)
        except Exception as e:
            handle_error(e)

    def encrypt_data(self):
        try:
            encrypted_data = encrypt_data(self.contact_list, self.sorting_criteria)
            return encrypted_data
        except Exception as e:
            handle_error(e)

    def integrate_with_cms(self):
        try:
            integrate_with_cms(self.contact_list, self.sorting_criteria)
        except Exception as e:
            handle_error(e)
```