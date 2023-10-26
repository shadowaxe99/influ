```python
from src.sorting import sort_contacts
from src.error_handling import handle_error

def is_consistent_sorting(contact_list, sorting_criteria):
    """
    Function to check if the sorting is consistent.
    """
    try:
        # Sort the contacts
        sorted_contacts = sort_contacts(contact_list, sorting_criteria)

        # Check if the sorted contacts are in the correct order
        for i in range(len(sorted_contacts) - 1):
            for criterion in sorting_criteria:
                if sorted_contacts[i][criterion] > sorted_contacts[i + 1][criterion]:
                    return False
                elif sorted_contacts[i][criterion] < sorted_contacts[i + 1][criterion]:
                    break

        return True
    except Exception as e:
        handle_error(e)

def test_reliability():
    """
    Function to test the reliability of the sorting feature.
    """
    # Define a list of contacts and sorting criteria for testing
    contact_list = [
        {"first_name": "John", "last_name": "Doe", "company_name": "Company A"},
        {"first_name": "Jane", "last_name": "Doe", "company_name": "Company B"},
        {"first_name": "John", "last_name": "Smith", "company_name": "Company A"},
        {"first_name": "Jane", "last_name": "Smith", "company_name": "Company B"}
    ]
    sorting_criteria = ["last_name", "first_name", "company_name"]

    # Check if the sorting is consistent
    assert is_consistent_sorting(contact_list, sorting_criteria), "The sorting is not consistent."

    print("The reliability test passed successfully.")
```