```python
import threading
from src.sorting import sort_contacts

class RealTimeSorting:
    def __init__(self):
        self.sorting_thread = None

    def start_sorting(self, contact_list, sorting_criteria):
        if self.sorting_thread is not None and self.sorting_thread.is_alive():
            self.sorting_thread.join()

        self.sorting_thread = threading.Thread(target=self._sort_in_background, args=(contact_list, sorting_criteria))
        self.sorting_thread.start()

    def _sort_in_background(self, contact_list, sorting_criteria):
        sort_contacts(contact_list, sorting_criteria)

    def is_sorting_in_progress(self):
        return self.sorting_thread is not None and self.sorting_thread.is_alive()
```