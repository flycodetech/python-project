# ### 7. Check Balanced Parentheses
# **Problem:** Check if a string has balanced parentheses.

# **Solution:**
# ```python


def is_balanced(expr):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in expr:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or mapping[char] != stack.pop():
                return False
    return not stack
print(is_balanced("()[]{}"))
# ```


age = 18
def is_age():
    if age > 15:
        print(f'I am {age} old ')
is_age()

# ### 8. Prime Number Check
# **Problem:** Determine if a number is a prime.

# **Solution:**
# ```python
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
# ```

n = 5  # Define n with a value
print(is_prime(n))


# ### 9. Top K Frequent Elements
# **Problem:** Find the k most frequent elements in a list.

# **Solution:**
# ```python

from collections import Counter

def top_k_frequent(nums, k):
    return [item for item, _ in Counter(nums).most_common(k)]

print(top_k_frequent([1,1,1,2,2,3], 2))
# ```

# ### 10. Reverse Words in String
# **Problem:** Reverse the order of words in a string.

# **Solution:**
# ```python
def reverse_words(s):
    return ' '.join(s.split()[::-1])
print(reverse_words("Hello World!"))
# ```

# ### 11. Check for Palindrome
# **Problem:** Check if a string reads the same backward as forward.

# **Solution:**
# ```python
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("ratar"))
# ```

# ### 12. Find the Missing Number
# **Problem:** Find the missing number in a list of consecutive integers from 1 to n.

# **Solution:**
# ```python
def missing_number(arr):
    n = len(arr) + 1
    return n * (n + 1) // 2 - sum(arr)
print(missing_number([1, 2, 4, 5, 9]))
# ```
# ### 14. Check for Anagram
# **Problem:** Determine if two strings are anagrams.

# **Solution:**
# ```python
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)
print(is_anagram("listen", "silent"))
# ```
# **Problem:** Flatten a nested list using recursion.

# **Solution:**
# ```python
def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result += flatten(i)
        else:
            result.append(i)
    return result
lst = [[1, 2, [3, 4]], [5, 6], 7]  # Example nested list
print(flatten(lst))

# ### 16. Find Duplicates in List
# **Problem:** Return all duplicate elements in a list.

# **Solution:**
# ```python
from collections import Counter

def find_duplicates(lst):
    return [item for item, count in Counter(lst).items() if count > 1]

lst = [1, 2, 3, 4, 3, 4, 5, 6, 7] 

print(find_duplicates(lst))


# ```

# ### 17. Check Balanced Parentheses
# **Problem:** Check if a string has balanced parentheses.

# **Solution:**
# ```python
def is_balanced(expr):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in expr:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or mapping[char] != stack.pop():
                return False
    return not stack
print(is_balanced("()[]{}"))
# ```

# ```







# def is_drive():
#     if 18 == 18:
#         print('i m driving ')
#     elif  18 < 17:
#         print('its not yet time ')
#     else: 
#         18 >=19
#         print('i m not driving')


# is_drive()
    
    