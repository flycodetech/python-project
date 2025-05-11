# Here's a Python solution to the Two Sum problem using a hash map (dictionary) for efficient lookup:

# ✅ Solution
# python

def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], i]
        lookup[num] = i


### 1. Two Sum
# **Problem:** Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# **Solution:**
# ```python
def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i
# ```

### 2. Valid Parentheses
# **Problem:** Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# **Solution:**
# ```python
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or mapping[char] != stack.pop():
                return False
    return not stack
# ```

# ### 3. Merge Two Sorted Lists
# **Problem:** Merge two sorted linked lists and return it as a new sorted list.

# **Solution:**
# ```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    dummy = ListNode()
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 or l2
    return dummy.next
# ```

### 4. Best Time to Buy and Sell Stock
# **Problem:** Find the maximum profit you can achieve by buying and selling a stock.

# **Solution:**
# ```python
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit
# ```

### 5. Valid Anagram
# **Problem:** Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# **Solution:**
# ```python
from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)
# ```

### 6. Climbing Stairs
# **Problem:** You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps.

# **Solution:**
# ```python
def climb_stairs(n):
    a, b = 1, 1
    for _ in range(n-1):
        a, b = b, a + b
    return b
# ```

# ### 7. Majority Element
# **Problem:** Find the majority element that appears more than n/2 times in the array.

# **Solution:**
# ```python
def majority_element(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate
# ```

# ### 8. Remove Duplicates from Sorted Array
# **Problem:** Remove duplicates in-place from a sorted array.

# **Solution:**
# ```python
def remove_duplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1
# ```

# ### 9. Maximum Subarray
# **Problem:** Find the contiguous subarray with the largest sum.

# **Solution:**
# ```python
def max_sub_array(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
# ```

# ### 10. Reverse Linked List
# **Problem:** Reverse a singly linked list.

# **Solution:**
# ```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev
# ```

# ### 11. Two Sum
# **Problem:** Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# **Solution:**
# ```python
def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i
# ```

# ### 12. Valid Parentheses
# **Problem:** Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# **Solution:**
# ```python
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or mapping[char] != stack.pop():
                return False
    return not stack
# ```

# ### 13. Merge Two Sorted Lists
# **Problem:** Merge two sorted linked lists and return it as a new sorted list.

# **Solution:**
# ```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    dummy = ListNode()
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 or l2
    return dummy.next
# ```

# ### 14. Best Time to Buy and Sell Stock
# **Problem:** Find the maximum profit you can achieve by buying and selling a stock.

# **Solution:**
# ```python
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit
# ```

# ### 15. Valid Anagram
# **Problem:** Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# **Solution:**
# ```python
from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)
# ```

# ### 16. Climbing Stairs
# **Problem:** You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps.

# **Solution:**
# ```python
def climb_stairs(n):
    a, b = 1, 1
    for _ in range(n-1):
        a, b = b, a + b
    return b
# ```

# ### 17. Majority Element
# **Problem:** Find the majority element that appears more than n/2 times in the array.

# **Solution:**
# ```python
def majority_element(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate
# ```

# ### 18. Remove Duplicates from Sorted Array
# **Problem:** Remove duplicates in-place from a sorted array.

# **Solution:**
# ```python
def remove_duplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1
# ```

# ### 19. Maximum Subarray
# **Problem:** Find the contiguous subarray with the largest sum.

# **Solution:**
# ```python
def max_sub_array(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
# ```

# ### 20. Reverse Linked List
# **Problem:** Reverse a singly linked list.

# **Solution:**
# ```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev
# ```

# ### 21. Two Sum
# **Problem:** Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# **Solution:**
# ```python
def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i
# ```

# ### 22. Valid Parentheses
# **Problem:** Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# **Solution:**
# ```python
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or mapping[char] != stack.pop():
                return False
    return not stack
# ```

# ### 23. Merge Two Sorted Lists
# **Problem:** Merge two sorted linked lists and return it as a new sorted list.

# **Solution:**
# ```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    dummy = ListNode()
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 or l2
    return dummy.next
# ```

# ### 24. Best Time to Buy and Sell Stock
# **Problem:** Find the maximum profit you can achieve by buying and selling a stock.

# **Solution:**
# ```python
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit
# ```

# ### 25. Valid Anagram
# **Problem:** Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# **Solution:**
# ```python
from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)
# ```

# ### 26. Climbing Stairs
# **Problem:** You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps.

# **Solution:**
# ```python
def climb_stairs(n):
    a, b = 1, 1
    for _ in range(n-1):
        a, b = b, a + b
    return b
# ```

# ### 27. Majority Element
# **Problem:** Find the majority element that appears more than n/2 times in the array.

# **Solution:**
# ```python
def majority_element(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate
# ```

# ### 28. Remove Duplicates from Sorted Array
# **Problem:** Remove duplicates in-place from a sorted array.

# **Solution:**
# ```python
def remove_duplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1
# ```

# ### 29. Maximum Subarray
# **Problem:** Find the contiguous subarray with the largest sum.

# **Solution:**
# ```python
def max_sub_array(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
# ```

# ### 30. Reverse Linked List
# **Problem:** Reverse a singly linked list.

# **Solution:**
# ```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev
# ```

# ### 31. Two Sum
# **Problem:** Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# **Solution:**
# ```python
def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i
# ```

# ### 32. Valid Parentheses
# **Problem:** Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# **Solution:**
# ```python
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or mapping[char] != stack.pop():
                return False
    return not stack
# ```

# ### 33. Merge Two Sorted Lists
# **Problem:** Merge two sorted linked lists and return it as a new sorted list.

# **Solution:**
# ```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    dummy = ListNode()
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 or l2
    return dummy.next
# ```

# ### 34. Best Time to Buy and Sell Stock
# **Problem:** Find the maximum profit you can achieve by buying and selling a stock.

# **Solution:**
# ```python
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit
# ```

# ### 35. Valid Anagram
# **Problem:** Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# **Solution:**
# ```python
from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)
# ```

# ### 36. Climbing Stairs
# **Problem:** You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps.

# **Solution:**
# ```python
def climb_stairs(n):
    a, b = 1, 1
    for _ in range(n-1):
        a, b = b, a + b
    return b
# ```

# ### 37. Majority Element
# **Problem:** Find the majority element that appears more than n/2 times in the array.

# **Solution:**
# ```python
def majority_element(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate
# ```

# ### 38. Remove Duplicates from Sorted Array
# **Problem:** Remove duplicates in-place from a sorted array.

# **Solution:**
# ```python
def remove_duplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1
# ```

# ### 39. Maximum Subarray
# **Problem:** Find the contiguous subarray with the largest sum.

# **Solution:**
# ```python
def max_sub_array(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
# ```

# ### 40. Reverse Linked List
# **Problem:** Reverse a singly linked list.

# **Solution:**
# ```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev
# ```

# ### 41. Two Sum
# **Problem:** Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# **Solution:**
# ```python
def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i
# ```

# ### 42. Valid Parentheses
# **Problem:** Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# **Solution:**
# ```python
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or mapping[char] != stack.pop():
                return False
    return not stack
# ```

# ### 43. Merge Two Sorted Lists
# **Problem:** Merge two sorted linked lists and return it as a new sorted list.

# **Solution:**
# ```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    dummy = ListNode()
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 or l2
    return dummy.next
# ```

# ### 44. Best Time to Buy and Sell Stock
# **Problem:** Find the maximum profit you can achieve by buying and selling a stock.

# **Solution:**
# ```python
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit
# ```

# ### 45. Valid Anagram
# **Problem:** Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# **Solution:**
# ```python
from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)
# ```

# ### 46. Climbing Stairs
# **Problem:** You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps.

# **Solution:**
# ```python
def climb_stairs(n):
    a, b = 1, 1
    for _ in range(n-1):
        a, b = b, a + b
    return b
# ```

# ### 47. Majority Element
# **Problem:** Find the majority element that appears more than n/2 times in the array.

# **Solution:**
# ```python
def majority_element(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate
# ```

# ### 48. Remove Duplicates from Sorted Array
# **Problem:** Remove duplicates in-place from a sorted array.

# **Solution:**
# ```python
def remove_duplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1
# ```

# ### 49. Maximum Subarray
# **Problem:** Find the contiguous subarray with the largest sum.

# **Solution:**
# ```python
def max_sub_array(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
# ```

# ### 50. Reverse Linked List
# **Problem:** Reverse a singly linked list.

# **Solution:**
# ```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev
# ```

# ### 51. Two Sum
# **Problem:** Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# **Solution:**
# ```python
def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i
# ```

# ### 52. Valid Parentheses
# **Problem:** Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# **Solution:**
# ```python
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or mapping[char] != stack.pop():
                return False
    return not stack
# ```

# ### 53. Merge Two Sorted Lists
# **Problem:** Merge two sorted linked lists and return it as a new sorted list.

# **Solution:**
# ```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    dummy = ListNode()
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 or l2
    return dummy.next
# ```

# ### 54. Best Time to Buy and Sell Stock
# **Problem:** Find the maximum profit you can achieve by buying and selling a stock.

# **Solution:**
# ```python
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit
# ```

# ### 55. Valid Anagram
# **Problem:** Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# **Solution:**
# ```python
from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)
# ```

# ### 56. Climbing Stairs
# **Problem:** You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps.

# **Solution:**
# ```python
def climb_stairs(n):
    a, b = 1, 1
    for _ in range(n-1):
        a, b = b, a + b
    return b
# ```

# ### 57. Majority Element
# **Problem:** Find the majority element that appears more than n/2 times in the array.

# **Solution:**
# ```python
def majority_element(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate
# ```

# ### 58. Remove Duplicates from Sorted Array
# **Problem:** Remove duplicates in-place from a sorted array.

# **Solution:**
# ```python
def remove_duplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1
# ```

# ### 59. Maximum Subarray
# **Problem:** Find the contiguous subarray with the largest sum.

# **Solution:**
# ```python
def max_sub_array(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
# ```

# ### 60. Reverse Linked List
# **Problem:** Reverse a singly linked list.

# **Solution:**
# ```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev
# ```

# ### 61. Two Sum
# **Problem:** Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# **Solution:**
# ```python
def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i
# ```

# ### 62. Valid Parentheses
# **Problem:** Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# **Solution:**
# ```python
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or mapping[char] != stack.pop():
                return False
    return not stack
# ```

# ### 63. Merge Two Sorted Lists
# **Problem:** Merge two sorted linked lists and return it as a new sorted list.

# **Solution:**
# ```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    dummy = ListNode()
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 or l2
    return dummy.next
# ```

# ### 64. Best Time to Buy and Sell Stock
# **Problem:** Find the maximum profit you can achieve by buying and selling a stock.

# **Solution:**
# ```python
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit
# ```

# ### 65. Valid Anagram
# **Problem:** Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# **Solution:**
# ```python
from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)
# ```

# ### 66. Climbing Stairs
# **Problem:** You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps.

# **Solution:**
# ```python
def climb_stairs(n):
    a, b = 1, 1
    for _ in range(n-1):
        a, b = b, a + b
    return b
# ```

# ### 67. Majority Element
# **Problem:** Find the majority element that appears more than n/2 times in the array.

# **Solution:**
# ```python
def majority_element(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate
# ```

# ### 68. Remove Duplicates from Sorted Array
# **Problem:** Remove duplicates in-place from a sorted array.

# **Solution:**
# ```python
def remove_duplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1
# ```

# ### 69. Maximum Subarray
# **Problem:** Find the contiguous subarray with the largest sum.

# **Solution:**
# ```python
def max_sub_array(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
# ```

# ### 70. Reverse Linked List
# **Problem:** Reverse a singly linked list.

# **Solution:**
# ```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev
# ```

# ### 71. Two Sum
# **Problem:** Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# **Solution:**
# ```python
def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i
# ```

# ### 72. Valid Parentheses
# **Problem:** Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# **Solution:**
# ```python
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or mapping[char] != stack.pop():
                return False
    return not stack
# ```

# ### 73. Merge Two Sorted Lists
# **Problem:** Merge two sorted linked lists and return it as a new sorted list.

# **Solution:**
# ```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    dummy = ListNode()
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 or l2
    return dummy.next
# ```

# ### 74. Best Time to Buy and Sell Stock
# **Problem:** Find the maximum profit you can achieve by buying and selling a stock.

# **Solution:**
# ```python
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit
# ```

# ### 75. Valid Anagram
# **Problem:** Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# **Solution:**
# ```python
from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)
# ```

# ### 76. Climbing Stairs
# **Problem:** You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps.

# **Solution:**
# ```python
def climb_stairs(n):
    a, b = 1, 1
    for _ in range(n-1):
        a, b = b, a + b
    return b
# ```

# ### 77. Majority Element
# **Problem:** Find the majority element that appears more than n/2 times in the array.

# **Solution:**
# ```python
def majority_element(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate
# ```

# ### 78. Remove Duplicates from Sorted Array
# **Problem:** Remove duplicates in-place from a sorted array.

# **Solution:**
# ```python
def remove_duplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1
# ```

# ### 79. Maximum Subarray
# **Problem:** Find the contiguous subarray with the largest sum.

# **Solution:**
# ```python
def max_sub_array(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
# ```

# ### 80. Reverse Linked List
# **Problem:** Reverse a singly linked list.

# **Solution:**
# ```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev
# ```

# ### 81. Two Sum
# **Problem:** Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# **Solution:**
# ```python
def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i
# ```

# ### 82. Valid Parentheses
# **Problem:** Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# **Solution:**
# ```python
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or mapping[char] != stack.pop():
                return False
    return not stack
# ```

# ### 83. Merge Two Sorted Lists
# **Problem:** Merge two sorted linked lists and return it as a new sorted list.

# **Solution:**
# ```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    dummy = ListNode()
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 or l2
    return dummy.next
# ```

# ### 84. Best Time to Buy and Sell Stock
# **Problem:** Find the maximum profit you can achieve by buying and selling a stock.

# **Solution:**
# ```python
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit
# ```

# ### 85. Valid Anagram
# **Problem:** Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# **Solution:**
# ```python
from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)
# ```

# ### 86. Climbing Stairs
# **Problem:** You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps.

# **Solution:**
# ```python
def climb_stairs(n):
    a, b = 1, 1
    for _ in range(n-1):
        a, b = b, a + b
    return b
# ```

# ### 87. Majority Element
# **Problem:** Find the majority element that appears more than n/2 times in the array.

# **Solution:**
# ```python
def majority_element(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate
# ```

# ### 88. Remove Duplicates from Sorted Array
# **Problem:** Remove duplicates in-place from a sorted array.

# **Solution:**
# ```python
def remove_duplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1
# ```

# ### 89. Maximum Subarray
# **Problem:** Find the contiguous subarray with the largest sum.

# **Solution:**
# ```python
def max_sub_array(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
# ```

# ### 90. Reverse Linked List
# **Problem:** Reverse a singly linked list.

# **Solution:**
# ```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev
# ```

# ### 91. Two Sum
# **Problem:** Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# **Solution:**
# ```python
def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i
# ```

# ### 92. Valid Parentheses
# **Problem:** Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# **Solution:**
# ```python
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or mapping[char] != stack.pop():
                return False
    return not stack
# ```

# ### 93. Merge Two Sorted Lists
# **Problem:** Merge two sorted linked lists and return it as a new sorted list.

# **Solution:**
# ```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    dummy = ListNode()
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 or l2
    return dummy.next
# ```

# ### 94. Best Time to Buy and Sell Stock
# **Problem:** Find the maximum profit you can achieve by buying and selling a stock.

# **Solution:**
# ```python
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit
# ```

# ### 95. Valid Anagram
# **Problem:** Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# **Solution:**
# ```python
from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)
# ```

# ### 96. Climbing Stairs
# **Problem:** You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps.

# **Solution:**
# ```python
def climb_stairs(n):
    a, b = 1, 1
    for _ in range(n-1):
        a, b = b, a + b
    return b
# ```

# ### 97. Majority Element
# **Problem:** Find the majority element that appears more than n/2 times in the array.

# **Solution:**
# ```python
def majority_element(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate
# ```

# ### 98. Remove Duplicates from Sorted Array
# **Problem:** Remove duplicates in-place from a sorted array.

# **Solution:**
# ```python
def remove_duplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1
# ```

# ### 99. Maximum Subarray
# **Problem:** Find the contiguous subarray with the largest sum.

# **Solution:**
# ```python
def max_sub_array(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
# ```

# ### 100. Reverse Linked List
# **Problem:** Reverse a singly linked list.

# **Solution:**
# ```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev
# ```

# ### 101. Two Sum
# **Problem:** Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# **Solution:**
# ```python
def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i
# ```

# ### 102. Valid Parentheses
# **Problem:** Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# **Solution:**
# ```python
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or mapping[char] != stack.pop():
                return False
    return not stack
# ```

# ### 103. Merge Two Sorted Lists
# **Problem:** Merge two sorted linked lists and return it as a new sorted list.

# **Solution:**
# ```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    dummy = ListNode()
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 or l2
    return dummy.next
# ```

# ### 104. Best Time to Buy and Sell Stock
# **Problem:** Find the maximum profit you can achieve by buying and selling a stock.

# **Solution:**
# ```python
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit
# ```

# ### 105. Valid Anagram
# **Problem:** Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# **Solution:**
# ```python
from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)
# ```

# ### 106. Climbing Stairs
# **Problem:** You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps.

# **Solution:**
# ```python
def climb_stairs(n):
    a, b = 1, 1
    for _ in range(n-1):
        a, b = b, a + b
    return b
# ```

# ### 107. Majority Element
# **Problem:** Find the majority element that appears more than n/2 times in the array.

# **Solution:**
# ```python
def majority_element(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate
# ```

# ### 108. Remove Duplicates from Sorted Array
# **Problem:** Remove duplicates in-place from a sorted array.

# **Solution:**
# ```python
def remove_duplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1
# ```

# ### 109. Maximum Subarray
# **Problem:** Find the contiguous subarray with the largest sum.

# **Solution:**
# ```python
def max_sub_array(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
# ```

# ### 110. Reverse Linked List
# **Problem:** Reverse a singly linked list.

# **Solution:**
# ```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev
# ```

# ### 111. Two Sum
# **Problem:** Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# **Solution:**
# ```python
def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i
# ```

# ### 112. Valid Parentheses
# **Problem:** Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# **Solution:**
# ```python
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or mapping[char] != stack.pop():
                return False
    return not stack
# ```

# ### 113. Merge Two Sorted Lists
# **Problem:** Merge two sorted linked lists and return it as a new sorted list.

# **Solution:**
# ```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    dummy = ListNode()
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 or l2
    return dummy.next
# ```

# ### 114. Best Time to Buy and Sell Stock
# **Problem:** Find the maximum profit you can achieve by buying and selling a stock.

# **Solution:**
# ```python
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit
# ```

# ### 115. Valid Anagram
# **Problem:** Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# **Solution:**
# ```python
from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)
# ```

# ### 116. Climbing Stairs
# **Problem:** You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps.

# **Solution:**
# ```python
def climb_stairs(n):
    a, b = 1, 1
    for _ in range(n-1):
        a, b = b, a + b
    return b
# ```

# ### 117. Majority Element
# **Problem:** Find the majority element that appears more than n/2 times in the array.

# **Solution:**
# ```python
def majority_element(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate
# ```

# ### 118. Remove Duplicates from Sorted Array
# **Problem:** Remove duplicates in-place from a sorted array.

# **Solution:**
# ```python
def remove_duplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1
# ```

# ### 119. Maximum Subarray
# **Problem:** Find the contiguous subarray with the largest sum.

# **Solution:**
# ```python
def max_sub_array(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
# ```

# ### 120. Reverse Linked List
# **Problem:** Reverse a singly linked list.

# **Solution:**
# ```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev
# ```

# ### 121. Two Sum
# **Problem:** Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# **Solution:**
# ```python
def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i
# ```

# ### 122. Valid Parentheses
# **Problem:** Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# **Solution:**
# ```python
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or mapping[char] != stack.pop():
                return False
    return not stack
# ```

# ### 123. Merge Two Sorted Lists
# **Problem:** Merge two sorted linked lists and return it as a new sorted list.

# **Solution:**
# ```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    dummy = ListNode()
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 or l2
    return dummy.next
# ```

# ### 124. Best Time to Buy and Sell Stock
# **Problem:** Find the maximum profit you can achieve by buying and selling a stock.

# **Solution:**
# ```python
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit
# ```

# ### 125. Valid Anagram
# **Problem:** Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# **Solution:**
# ```python
from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)
# ```

# ### 126. Climbing Stairs
# **Problem:** You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps.

# **Solution:**
# ```python
def climb_stairs(n):
    a, b = 1, 1
    for _ in range(n-1):
        a, b = b, a + b
    return b
# ```

# ### 127. Majority Element
# **Problem:** Find the majority element that appears more than n/2 times in the array.

# **Solution:**
# ```python
def majority_element(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate
# ```

# ### 128. Remove Duplicates from Sorted Array
# **Problem:** Remove duplicates in-place from a sorted array.

# **Solution:**
# ```python
def remove_duplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1
# ```

# ### 129. Maximum Subarray
# **Problem:** Find the contiguous subarray with the largest sum.

# **Solution:**
# ```python
def max_sub_array(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
# ```

# ### 130. Reverse Linked List
# **Problem:** Reverse a singly linked list.

# **Solution:**
# ```python
# class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev
# ```

### 131. Two Sum
# **Problem:** Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# **Solution:**
# ```python
def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i
# ```

### 132. Valid Parentheses
# **Problem:** Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# **Solution:**
# ```python
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or mapping[char] != stack.pop():
                return False
    return not stack
# ```

### 133. Merge Two Sorted Lists
# **Problem:** Merge two sorted linked lists and return it as a new sorted list.

# **Solution:**
# ```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    dummy = ListNode()
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 or l2
    return dummy.next
# ```

### 134. Best Time to Buy and Sell Stock
# **Problem:** Find the maximum profit you can achieve by buying and selling a stock.

# **Solution:**
# ```python
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit
# ```

### 135. Valid Anagram
# **Problem:** Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# **Solution:**
# ```python
from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)
# ```

### 136. Climbing Stairs
# **Problem:** You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps.

# **Solution:**
# ```python
def climb_stairs(n):
    a, b = 1, 1
    for _ in range(n-1):
        a, b = b, a + b
    return b
# ```

### 137. Majority Element
# **Problem:** Find the majority element that appears more than n/2 times in the array.

# **Solution:**
# ```python
def majority_element(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate
# ```

### 138. Remove Duplicates from Sorted Array
# **Problem:** Remove duplicates in-place from a sorted array.

# **Solution:**
# ```python
def remove_duplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1
# ```

### 139. Maximum Subarray
# **Problem:** Find the contiguous subarray with the largest sum.

# **Solution:**
# ```python
def max_sub_array(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
# ```

### 140. Reverse Linked List
# **Problem:** Reverse a singly linked list.

# **Solution:**
# ```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev
# ```

### 141. Two Sum
# **Problem:** Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# **Solution:**
# ```python
def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i
# ```

### 142. Valid Parentheses
# **Problem:** Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# **Solution:**
# ```python
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or mapping[char] != stack.pop():
                return False
    return not stack
# ```

### 143. Merge Two Sorted Lists
# **Problem:** Merge two sorted linked lists and return it as a new sorted list.

# **Solution:**
# ```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    dummy = ListNode()
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 or l2
    return dummy.next
# ```

### 144. Best Time to Buy and Sell Stock
# **Problem:** Find the maximum profit you can achieve by buying and selling a stock.

# **Solution:**
# ```python
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit
# ```

### 145. Valid Anagram
# **Problem:** Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# **Solution:**
# ```python
from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)
# ```

### 146. Climbing Stairs
# **Problem:** You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps.

# **Solution:**
# ```python
def climb_stairs(n):
    a, b = 1, 1
    for _ in range(n-1):
        a, b = b, a + b
    return b
# ```

### 147. Majority Element
# **Problem:** Find the majority element that appears more than n/2 times in the array.

# **Solution:**
# ```python
def majority_element(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate
# ```

### 148. Remove Duplicates from Sorted Array
# **Problem:** Remove duplicates in-place from a sorted array.

# **Solution:**
# ```python
def remove_duplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1
# ```

### 149. Maximum Subarray
# **Problem:** Find the contiguous subarray with the largest sum.

# **Solution:**
# ```python
def max_sub_array(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
# ```

### 150. Reverse Linked List
# **Problem:** Reverse a singly linked list.

# **Solution:**
# ```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev
# ```
