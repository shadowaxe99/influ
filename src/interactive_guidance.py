```python
class InteractiveGuidance:
    def __init__(self):
        self.guidance_messages = {
            "sort_request": "Sorting contacts based on your criteria...",
            "sort_complete": "Sorting complete! Your contacts have been sorted.",
            "error_message": "An error occurred during sorting. Please try again."
        }

    def display_message(self, message_name):
        print(self.guidance_messages.get(message_name, "Unknown message"))

    def guide_user(self):
        print("Welcome to the Complex Contacts Sorting feature!")
        print("Here, you can sort your contacts based on multiple criteria.")
        print("You can also create and save custom sorting profiles for future use.")
        print("Let's get started!")

    def guide_sorting(self):
        print("To sort your contacts, select your desired criteria from the dropdown menu.")
        print("You can select multiple criteria for a more refined sorting.")
        print("Once you've selected your criteria, click the 'Sort' button to sort your contacts.")

    def guide_profiles(self):
        print("To create a sorting profile, select your desired criteria and give your profile a name.")
        print("Once you've created a profile, you can quickly apply it to sort your contacts in the future.")
        print("To apply a profile, select it from the 'Profiles' dropdown menu and click 'Sort'.")

    def guide_preview(self):
        print("Before finalizing your sorting, you can preview how your contacts will appear.")
        print("If you're satisfied with the preview, click 'Confirm' to finalize the sorting.")
        print("If not, you can adjust your criteria and preview again.")

    def guide_error_handling(self):
        print("If an error occurs during sorting, don't worry!")
        print("Our system will handle the error and let you know what happened.")
        print("You can then adjust your criteria or try again.")
```
