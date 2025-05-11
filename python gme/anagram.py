# ### 4. Check for Anagram
# **Problem:** Determine if two strings are anagrams.

# **Solution:**
# ```python
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)
# ```