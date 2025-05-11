# ### 6. Find Duplicates in List
# **Problem:** Return all duplicate elements in a list.

# **Solution:**
# ```python
from collections import Counter

def find_duplicates(lst):
    lst = [11, 23,11,16, 16, 32, 23]
    return [item for item, count in Counter(lst).items() if count > 1]
# ```
print(find_duplicates(list))