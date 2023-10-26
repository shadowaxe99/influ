```python
def display_preview(contact_list, sorting_criteria):
    """
    Function to display a preview of the sorted contact list based on the selected sorting criteria.
    """
    # Sort the contact list based on the sorting criteria
    sorted_contacts = sorted(contact_list, key=lambda x: [x[criteria] for criteria in sorting_criteria])

    # Display the first 10 contacts in the sorted list as a preview
    for contact in sorted_contacts[:10]:
        print(f"First Name: {contact['first_name']}, Last Name: {contact['last_name']}, Company: {contact['company_name']}")

    return sorted_contacts
```