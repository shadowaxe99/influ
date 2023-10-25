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
        # Sort the contact list based on the provided criteria
        contact_list.sort(key=itemgetter(*sorting_criteria))
    except Exception as e:
        # Import error handling function from error_handling.py
        from error_handling import handle_error
        handle_error(e)
    return contact_list
```