```python
from tkinter import *
from src.sorting import sort_contacts
from src.profiles import load_profile, save_profile
from src.preview import display_preview

class UserInterface:
    def __init__(self, master):
        self.master = master
        master.title("Complex Contacts Sorting")

        self.sort_button = Button(master, text="Sort", command=self.sort_contacts)
        self.sort_button.pack()

        self.criteria_dropdown = OptionMenu(master, StringVar(), *sorting_criteria)
        self.criteria_dropdown.pack()

        self.profile_dropdown = OptionMenu(master, StringVar(), *sorting_profiles.keys())
        self.profile_dropdown.pack()

        self.preview_area = Text(master)
        self.preview_area.pack()

    def sort_contacts(self):
        selected_criteria = self.criteria_dropdown.get()
        selected_profile = self.profile_dropdown.get()

        if selected_profile:
            load_profile(selected_profile)
        else:
            sort_contacts(selected_criteria)

        sorted_contacts = display_preview()
        self.preview_area.insert(END, sorted_contacts)

root = Tk()
ui = UserInterface(root)
root.mainloop()
```
This code creates a simple user interface using Tkinter, a popular Python library for creating GUIs. The interface includes a button for triggering the sorting process, dropdown menus for selecting sorting criteria and profiles, and a text area for displaying a preview of the sorted list. The `sort_contacts` method is called when the sort button is clicked, and it either loads a user-defined sorting profile or sorts the contacts based on the selected criteria. The sorted contacts are then displayed in the preview area.