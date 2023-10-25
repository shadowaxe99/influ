```python
class SortingProfile:
    def __init__(self, profile_name, criteria):
        self.profile_name = profile_name
        self.criteria = criteria

sorting_profiles = {}

def save_profile(profile_name, criteria):
    sorting_profiles[profile_name] = SortingProfile(profile_name, criteria)

def load_profile(profile_name):
    if profile_name in sorting_profiles:
        return sorting_profiles[profile_name]
    else:
        raise Exception(f"No profile found with name {profile_name}")
```