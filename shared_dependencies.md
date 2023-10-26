1. Shared Variables:
   - `contact_list`: A list of all contacts that will be sorted.
   - `sorting_criteria`: A list of criteria selected by the user for sorting.
   - `sorting_profiles`: A dictionary of user-defined sorting profiles.

2. Data Schemas:
   - `Contact`: A schema representing a contact, including fields like `first_name`, `last_name`, `company_name`, etc.
   - `SortingProfile`: A schema representing a user-defined sorting profile, including fields like `profile_name` and `criteria`.

3. DOM Element IDs:
   - `sort_button`: The button that triggers the sorting process.
   - `criteria_dropdown`: The dropdown menu where users select sorting criteria.
   - `profile_dropdown`: The dropdown menu where users select a sorting profile.
   - `preview_area`: The area where the sorted list preview is displayed.

4. Message Names:
   - `sort_request`: A message sent when the user triggers a sort.
   - `sort_complete`: A message sent when the sorting process is complete.
   - `error_message`: A message sent when an error occurs during sorting.

5. Function Names:
   - `sort_contacts()`: A function in `sorting.py` that sorts the contacts based on the selected criteria.
   - `display_preview()`: A function in `preview.py` that displays a preview of the sorted list.
   - `save_profile()`: A function in `profiles.py` that saves a user-defined sorting profile.
   - `load_profile()`: A function in `profiles.py` that loads a user-defined sorting profile.
   - `encrypt_data()`: A function in `data_encryption.py` that encrypts contact data and sorting criteria.
   - `handle_error()`: A function in `error_handling.py` that handles errors during the sorting process.
   - `integrate_with_cms()`: A function in `integration.py` that integrates the sorting feature with the existing Contacts Management System.