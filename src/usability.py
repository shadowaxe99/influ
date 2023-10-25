```python
from src.preview import display_preview
from src.interactive_guidance import provide_guidance

def create_sorting_interface(contact_list, sorting_criteria, sorting_profiles):
    # Create the sorting interface
    sort_button = create_sort_button()
    criteria_dropdown = create_criteria_dropdown(sorting_criteria)
    profile_dropdown = create_profile_dropdown(sorting_profiles)
    preview_area = create_preview_area()

    # Attach event handlers
    sort_button.onclick = lambda: sort_contacts(contact_list, criteria_dropdown.value, profile_dropdown.value)
    criteria_dropdown.onchange = lambda: display_preview(contact_list, criteria_dropdown.value)
    profile_dropdown.onchange = lambda: load_profile(profile_dropdown.value)

    # Return the created interface
    return sort_button, criteria_dropdown, profile_dropdown, preview_area

def create_sort_button():
    # Create the sort button
    sort_button = Button(text="Sort")
    return sort_button

def create_criteria_dropdown(sorting_criteria):
    # Create the criteria dropdown
    criteria_dropdown = Dropdown(options=sorting_criteria)
    return criteria_dropdown

def create_profile_dropdown(sorting_profiles):
    # Create the profile dropdown
    profile_dropdown = Dropdown(options=sorting_profiles.keys())
    return profile_dropdown

def create_preview_area():
    # Create the preview area
    preview_area = TextArea()
    return preview_area

def sort_contacts(contact_list, criteria, profile):
    # Load the profile if one is selected
    if profile:
        criteria = load_profile(profile)

    # Sort the contacts
    sorted_contacts = sort_contacts_by_criteria(contact_list, criteria)

    # Display a preview of the sorted contacts
    display_preview(sorted_contacts)

    # Provide interactive guidance
    provide_guidance()
```