```python
from operator import itemgetter

def sort_contacts(contact_list, sorting_criteria):
    """
    Sorts the contact list based on the provided sorting criteria.
    :param contact_list: List of contacts to be sorted.
    :param sorting_criteria: List of criteria to sort by.
    :return: Sorted list of contacts.
    """
    try:
        # Sort the contacts based on the provided criteria
        sorted_contacts = sorted(contact_list, key=itemgetter(*sorting_criteria))
        return sorted_contacts
    except Exception as e:
        # If an error occurs during sorting, call the error handling function
        from error_handling import handle_error
        handle_error(e)

def apply_sorting_profile(contact_list, sorting_profile):
    """
    Applies a sorting profile to the contact list.
    :param contact_list: List of contacts to be sorted.
    :param sorting_profile: Sorting profile to apply.
    :return: Sorted list of contacts.
    """
    try:
        # Extract the sorting criteria from the profile
        sorting_criteria = sorting_profile['criteria']
        # Sort the contacts based on the profile's criteria
        sorted_contacts = sort_contacts(contact_list, sorting_criteria)
        return sorted_contacts
    except Exception as e:
        # If an error occurs during sorting, call the error handling function
        from error_handling import handle_error
        handle_error(e)
```