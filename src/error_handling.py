```python
class SortingError(Exception):
    """Base class for exceptions in this module."""
    pass

class CriteriaError(SortingError):
    """Exception raised for errors in the input sorting criteria.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message

class ProfileError(SortingError):
    """Exception raised for errors in the input sorting profile.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message

def handle_error(error):
    """Function to handle errors during the sorting process."""
    if isinstance(error, CriteriaError):
        print(f"Criteria Error: {error.message}")
    elif isinstance(error, ProfileError):
        print(f"Profile Error: {error.message}")
    else:
        print(f"Unexpected Error: {error}")
```