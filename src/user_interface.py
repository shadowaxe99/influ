```python
import tkinter as tk
from tkinter import ttk
from sorting import sort_contacts
from preview import display_preview
from profiles import save_profile, load_profile

class UserInterface:
    def __init__(self, root):
        self.root = root
        self.sorting_criteria = []
        self.sorting_profiles = {}

        # Create UI elements
        self.criteria_dropdown = ttk.Combobox(root)
        self.profile_dropdown = ttk.Combobox(root)
        self.sort_button = ttk.Button(root, text="Sort", command=self.sort_contacts)
        self.preview_area = tk.Text(root)

        # Populate dropdowns
        self.populate_criteria_dropdown()
        self.populate_profile_dropdown()

    def populate_criteria_dropdown(self):
        # This is a placeholder. Replace with actual criteria.
        criteria = ["First Name", "Last Name", "Company Name"]
        self.criteria_dropdown['values'] = criteria

    def populate_profile_dropdown(self):
        # This is a placeholder. Replace with actual profiles.
        profiles = ["Business", "Personal"]
        self.profile_dropdown['values'] = profiles

    def sort_contacts(self):
        # Get selected criteria and profile
        selected_criteria = self.criteria_dropdown.get()
        selected_profile = self.profile_dropdown.get()

        # Load profile if selected
        if selected_profile:
            self.sorting_criteria = load_profile(selected_profile)
        else:
            self.sorting_criteria.append(selected_criteria)

        # Sort contacts
        sorted_contacts = sort_contacts(self.sorting_criteria)

        # Display preview
        display_preview(sorted_contacts, self.preview_area)

    def save_profile(self, profile_name):
        # Save current sorting criteria as a profile
        save_profile(profile_name, self.sorting_criteria)

if __name__ == "__main__":
    root = tk.Tk()
    ui = UserInterface(root)
    root.mainloop()
```