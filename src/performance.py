```python
import time
from src.sorting import sort_contacts

def measure_performance(contact_list, sorting_criteria):
    start_time = time.time()
    
    # Call the sorting function and measure its execution time
    sort_contacts(contact_list, sorting_criteria)
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    # Check if the sorting operation was completed within the expected time frame
    if execution_time > 300:  # 300 seconds = 5 minutes
        raise PerformanceException("Sorting operation exceeded the expected time limit.")
    
    return execution_time

class PerformanceException(Exception):
    pass
```