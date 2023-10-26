```python
# src/supportability.py

class Supportability:
    def __init__(self):
        self.contact_list = []
        self.sorting_criteria = []
        self.sorting_profiles = {}

    def add_contact(self, contact):
        self.contact_list.append(contact)

    def set_sorting_criteria(self, criteria):
        self.sorting_criteria = criteria

    def add_sorting_profile(self, profile_name, criteria):
        self.sorting_profiles[profile_name] = criteria

    def get_contact_list(self):
        return self.contact_list

    def get_sorting_criteria(self):
        return self.sorting_criteria

    def get_sorting_profiles(self):
        return self.sorting_profiles

    def update_contact(self, contact):
        for i, existing_contact in enumerate(self.contact_list):
            if existing_contact['id'] == contact['id']:
                self.contact_list[i] = contact
                break

    def update_sorting_profile(self, profile_name, criteria):
        self.sorting_profiles[profile_name] = criteria

    def delete_contact(self, contact_id):
        self.contact_list = [contact for contact in self.contact_list if contact['id'] != contact_id]

    def delete_sorting_profile(self, profile_name):
        if profile_name in self.sorting_profiles:
            del self.sorting_profiles[profile_name]
```