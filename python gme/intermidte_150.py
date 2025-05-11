### 1. Check for Palindrome
**Problem:** Check if a string reads the same backward as forward.

**Solution:**
```python
def is_palindrome(s):
    return s == s[::-1]
```

### 2. Find the Missing Number
**Problem:** Find the missing number in a list of consecutive integers from 1 to n.

**Solution:**
```python
def missing_number(arr):
    n = len(arr) + 1
    return n * (n + 1) // 2 - sum(arr)
```

### 3. Fibonacci Generator
**Problem:** Generate the first n Fibonacci numbers.

**Solution:**
```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
```

### 4. Check for Anagram
**Problem:** Determine if two strings are anagrams.

**Solution:**
```python
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)
```

### 5. Flatten Nested List
**Problem:** Flatten a nested list using recursion.

**Solution:**
```python
def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result += flatten(i)
        else:
            result.append(i)
    return result
```

### 6. Find Duplicates in List
**Problem:** Return all duplicate elements in a list.

**Solution:**
```python
from collections import Counter

def find_duplicates(lst):
    return [item for item, count in Counter(lst).items() if count > 1]
```

### 7. Check Balanced Parentheses
**Problem:** Check if a string has balanced parentheses.

**Solution:**
```python
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
```

### 8. Prime Number Check
**Problem:** Determine if a number is a prime.

**Solution:**
```python
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
```

### 9. Top K Frequent Elements
**Problem:** Find the k most frequent elements in a list.

**Solution:**
```python
from collections import Counter

def top_k_frequent(nums, k):
    return [item for item, _ in Counter(nums).most_common(k)]
```

### 10. Reverse Words in String
**Problem:** Reverse the order of words in a string.

**Solution:**
```python
def reverse_words(s):
    return ' '.join(s.split()[::-1]
```

### 11. Check for Palindrome
**Problem:** Check if a string reads the same backward as forward.

**Solution:**
```python
def is_palindrome(s):
    return s == s[::-1]
```

### 12. Find the Missing Number
**Problem:** Find the missing number in a list of consecutive integers from 1 to n.

**Solution:**
```python
def missing_number(arr):
    n = len(arr) + 1
    return n * (n + 1) // 2 - sum(arr)
```

### 13. Fibonacci Generator
**Problem:** Generate the first n Fibonacci numbers.

**Solution:**
```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
```

### 14. Check for Anagram
**Problem:** Determine if two strings are anagrams.

**Solution:**
```python
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)
```

### 15. Flatten Nested List
**Problem:** Flatten a nested list using recursion.

**Solution:**
```python
def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result += flatten(i)
        else:
            result.append(i)
    return result
```

### 16. Find Duplicates in List
**Problem:** Return all duplicate elements in a list.

**Solution:**
```python
from collections import Counter

def find_duplicates(lst):
    return [item for item, count in Counter(lst).items() if count > 1]
```

### 17. Check Balanced Parentheses
**Problem:** Check if a string has balanced parentheses.

**Solution:**
```python
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
```

### 18. Prime Number Check
**Problem:** Determine if a number is a prime.

**Solution:**
```python
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
```

### 19. Top K Frequent Elements
**Problem:** Find the k most frequent elements in a list.

**Solution:**
```python
from collections import Counter

def top_k_frequent(nums, k):
    return [item for item, _ in Counter(nums).most_common(k)]
```

### 20. Reverse Words in String
**Problem:** Reverse the order of words in a string.

**Solution:**
```python
def reverse_words(s):
    return ' '.join(s.split()[::-1]
```

### 21. Check for Palindrome
**Problem:** Check if a string reads the same backward as forward.

**Solution:**
```python
def is_palindrome(s):
    return s == s[::-1]
```

### 22. Find the Missing Number
**Problem:** Find the missing number in a list of consecutive integers from 1 to n.

**Solution:**
```python
def missing_number(arr):
    n = len(arr) + 1
    return n * (n + 1) // 2 - sum(arr)
```

### 23. Fibonacci Generator
**Problem:** Generate the first n Fibonacci numbers.

**Solution:**
```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
```

### 24. Check for Anagram
**Problem:** Determine if two strings are anagrams.

**Solution:**
```python
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)
```

### 25. Flatten Nested List
**Problem:** Flatten a nested list using recursion.

**Solution:**
```python
def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result += flatten(i)
        else:
            result.append(i)
    return result
```

### 26. Find Duplicates in List
**Problem:** Return all duplicate elements in a list.

**Solution:**
```python
from collections import Counter

def find_duplicates(lst):
    return [item for item, count in Counter(lst).items() if count > 1]
```

### 27. Check Balanced Parentheses
**Problem:** Check if a string has balanced parentheses.

**Solution:**
```python
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
```

### 28. Prime Number Check
**Problem:** Determine if a number is a prime.

**Solution:**
```python
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
```

### 29. Top K Frequent Elements
**Problem:** Find the k most frequent elements in a list.

**Solution:**
```python
from collections import Counter

def top_k_frequent(nums, k):
    return [item for item, _ in Counter(nums).most_common(k)]
```

### 30. Reverse Words in String
**Problem:** Reverse the order of words in a string.

**Solution:**
```python
def reverse_words(s):
    return ' '.join(s.split()[::-1]
```

### 31. Check for Palindrome
**Problem:** Check if a string reads the same backward as forward.

**Solution:**
```python
def is_palindrome(s):
    return s == s[::-1]
```

### 32. Find the Missing Number
**Problem:** Find the missing number in a list of consecutive integers from 1 to n.

**Solution:**
```python
def missing_number(arr):
    n = len(arr) + 1
    return n * (n + 1) // 2 - sum(arr)
```

### 33. Fibonacci Generator
**Problem:** Generate the first n Fibonacci numbers.

**Solution:**
```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
```

### 34. Check for Anagram
**Problem:** Determine if two strings are anagrams.

**Solution:**
```python
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)
```

### 35. Flatten Nested List
**Problem:** Flatten a nested list using recursion.

**Solution:**
```python
def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result += flatten(i)
        else:
            result.append(i)
    return result
```

### 36. Find Duplicates in List
**Problem:** Return all duplicate elements in a list.

**Solution:**
```python
from collections import Counter

def find_duplicates(lst):
    return [item for item, count in Counter(lst).items() if count > 1]
```

### 37. Check Balanced Parentheses
**Problem:** Check if a string has balanced parentheses.

**Solution:**
```python
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
```

### 38. Prime Number Check
**Problem:** Determine if a number is a prime.

**Solution:**
```python
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
```

### 39. Top K Frequent Elements
**Problem:** Find the k most frequent elements in a list.

**Solution:**
```python
from collections import Counter

def top_k_frequent(nums, k):
    return [item for item, _ in Counter(nums).most_common(k)]
```

### 40. Reverse Words in String
**Problem:** Reverse the order of words in a string.

**Solution:**
```python
def reverse_words(s):
    return ' '.join(s.split()[::-1]
```

### 41. Check for Palindrome
**Problem:** Check if a string reads the same backward as forward.

**Solution:**
```python
def is_palindrome(s):
    return s == s[::-1]
```

### 42. Find the Missing Number
**Problem:** Find the missing number in a list of consecutive integers from 1 to n.

**Solution:**
```python
def missing_number(arr):
    n = len(arr) + 1
    return n * (n + 1) // 2 - sum(arr)
```

### 43. Fibonacci Generator
**Problem:** Generate the first n Fibonacci numbers.

**Solution:**
```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
```

### 44. Check for Anagram
**Problem:** Determine if two strings are anagrams.

**Solution:**
```python
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)
```

### 45. Flatten Nested List
**Problem:** Flatten a nested list using recursion.

**Solution:**
```python
def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result += flatten(i)
        else:
            result.append(i)
    return result
```

### 46. Find Duplicates in List
**Problem:** Return all duplicate elements in a list.

**Solution:**
```python
from collections import Counter

def find_duplicates(lst):
    return [item for item, count in Counter(lst).items() if count > 1]
```

### 47. Check Balanced Parentheses
**Problem:** Check if a string has balanced parentheses.

**Solution:**
```python
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
```

### 48. Prime Number Check
**Problem:** Determine if a number is a prime.

**Solution:**
```python
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
```

### 49. Top K Frequent Elements
**Problem:** Find the k most frequent elements in a list.

**Solution:**
```python
from collections import Counter

def top_k_frequent(nums, k):
    return [item for item, _ in Counter(nums).most_common(k)]
```

### 50. Reverse Words in String
**Problem:** Reverse the order of words in a string.

**Solution:**
```python
def reverse_words(s):
    return ' '.join(s.split()[::-1]
```

### 51. Check for Palindrome
**Problem:** Check if a string reads the same backward as forward.

**Solution:**
```python
def is_palindrome(s):
    return s == s[::-1]
```

### 52. Find the Missing Number
**Problem:** Find the missing number in a list of consecutive integers from 1 to n.

**Solution:**
```python
def missing_number(arr):
    n = len(arr) + 1
    return n * (n + 1) // 2 - sum(arr)
```

### 53. Fibonacci Generator
**Problem:** Generate the first n Fibonacci numbers.

**Solution:**
```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
```

### 54. Check for Anagram
**Problem:** Determine if two strings are anagrams.

**Solution:**
```python
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)
```

### 55. Flatten Nested List
**Problem:** Flatten a nested list using recursion.

**Solution:**
```python
def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result += flatten(i)
        else:
            result.append(i)
    return result
```

### 56. Find Duplicates in List
**Problem:** Return all duplicate elements in a list.

**Solution:**
```python
from collections import Counter

def find_duplicates(lst):
    return [item for item, count in Counter(lst).items() if count > 1]
```

### 57. Check Balanced Parentheses
**Problem:** Check if a string has balanced parentheses.

**Solution:**
```python
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
```

### 58. Prime Number Check
**Problem:** Determine if a number is a prime.

**Solution:**
```python
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
```

### 59. Top K Frequent Elements
**Problem:** Find the k most frequent elements in a list.

**Solution:**
```python
from collections import Counter

def top_k_frequent(nums, k):
    return [item for item, _ in Counter(nums).most_common(k)]
```

### 60. Reverse Words in String
**Problem:** Reverse the order of words in a string.

**Solution:**
```python
def reverse_words(s):
    return ' '.join(s.split()[::-1]
```

### 61. Check for Palindrome
**Problem:** Check if a string reads the same backward as forward.

**Solution:**
```python
def is_palindrome(s):
    return s == s[::-1]
```

### 62. Find the Missing Number
**Problem:** Find the missing number in a list of consecutive integers from 1 to n.

**Solution:**
```python
def missing_number(arr):
    n = len(arr) + 1
    return n * (n + 1) // 2 - sum(arr)
```

### 63. Fibonacci Generator
**Problem:** Generate the first n Fibonacci numbers.

**Solution:**
```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
```

### 64. Check for Anagram
**Problem:** Determine if two strings are anagrams.

**Solution:**
```python
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)
```

### 65. Flatten Nested List
**Problem:** Flatten a nested list using recursion.

**Solution:**
```python
def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result += flatten(i)
        else:
            result.append(i)
    return result
```

### 66. Find Duplicates in List
**Problem:** Return all duplicate elements in a list.

**Solution:**
```python
from collections import Counter

def find_duplicates(lst):
    return [item for item, count in Counter(lst).items() if count > 1]
```

### 67. Check Balanced Parentheses
**Problem:** Check if a string has balanced parentheses.

**Solution:**
```python
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
```

### 68. Prime Number Check
**Problem:** Determine if a number is a prime.

**Solution:**
```python
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
```

### 69. Top K Frequent Elements
**Problem:** Find the k most frequent elements in a list.

**Solution:**
```python
from collections import Counter

def top_k_frequent(nums, k):
    return [item for item, _ in Counter(nums).most_common(k)]
```

### 70. Reverse Words in String
**Problem:** Reverse the order of words in a string.

**Solution:**
```python
def reverse_words(s):
    return ' '.join(s.split()[::-1]
```

### 71. Check for Palindrome
**Problem:** Check if a string reads the same backward as forward.

**Solution:**
```python
def is_palindrome(s):
    return s == s[::-1]
```

### 72. Find the Missing Number
**Problem:** Find the missing number in a list of consecutive integers from 1 to n.

**Solution:**
```python
def missing_number(arr):
    n = len(arr) + 1
    return n * (n + 1) // 2 - sum(arr)
```

### 73. Fibonacci Generator
**Problem:** Generate the first n Fibonacci numbers.

**Solution:**
```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
```

### 74. Check for Anagram
**Problem:** Determine if two strings are anagrams.

**Solution:**
```python
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)
```

### 75. Flatten Nested List
**Problem:** Flatten a nested list using recursion.

**Solution:**
```python
def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result += flatten(i)
        else:
            result.append(i)
    return result
```

### 76. Find Duplicates in List
**Problem:** Return all duplicate elements in a list.

**Solution:**
```python
from collections import Counter

def find_duplicates(lst):
    return [item for item, count in Counter(lst).items() if count > 1]
```

### 77. Check Balanced Parentheses
**Problem:** Check if a string has balanced parentheses.

**Solution:**
```python
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
```

### 78. Prime Number Check
**Problem:** Determine if a number is a prime.

**Solution:**
```python
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
```

### 79. Top K Frequent Elements
**Problem:** Find the k most frequent elements in a list.

**Solution:**
```python
from collections import Counter

def top_k_frequent(nums, k):
    return [item for item, _ in Counter(nums).most_common(k)]
```

### 80. Reverse Words in String
**Problem:** Reverse the order of words in a string.

**Solution:**
```python
def reverse_words(s):
    return ' '.join(s.split()[::-1]
```

### 81. Check for Palindrome
**Problem:** Check if a string reads the same backward as forward.

**Solution:**
```python
def is_palindrome(s):
    return s == s[::-1]
```

### 82. Find the Missing Number
**Problem:** Find the missing number in a list of consecutive integers from 1 to n.

**Solution:**
```python
def missing_number(arr):
    n = len(arr) + 1
    return n * (n + 1) // 2 - sum(arr)
```

### 83. Fibonacci Generator
**Problem:** Generate the first n Fibonacci numbers.

**Solution:**
```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
```

### 84. Check for Anagram
**Problem:** Determine if two strings are anagrams.

**Solution:**
```python
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)
```

### 85. Flatten Nested List
**Problem:** Flatten a nested list using recursion.

**Solution:**
```python
def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result += flatten(i)
        else:
            result.append(i)
    return result
```

### 86. Find Duplicates in List
**Problem:** Return all duplicate elements in a list.

**Solution:**
```python
from collections import Counter

def find_duplicates(lst):
    return [item for item, count in Counter(lst).items() if count > 1]
```

### 87. Check Balanced Parentheses
**Problem:** Check if a string has balanced parentheses.

**Solution:**
```python
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
```

### 88. Prime Number Check
**Problem:** Determine if a number is a prime.

**Solution:**
```python
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
```

### 89. Top K Frequent Elements
**Problem:** Find the k most frequent elements in a list.

**Solution:**
```python
from collections import Counter

def top_k_frequent(nums, k):
    return [item for item, _ in Counter(nums).most_common(k)]
```

### 90. Reverse Words in String
**Problem:** Reverse the order of words in a string.

**Solution:**
```python
def reverse_words(s):
    return ' '.join(s.split()[::-1]
```

### 91. Check for Palindrome
**Problem:** Check if a string reads the same backward as forward.

**Solution:**
```python
def is_palindrome(s):
    return s == s[::-1]
```

### 92. Find the Missing Number
**Problem:** Find the missing number in a list of consecutive integers from 1 to n.

**Solution:**
```python
def missing_number(arr):
    n = len(arr) + 1
    return n * (n + 1) // 2 - sum(arr)
```

### 93. Fibonacci Generator
**Problem:** Generate the first n Fibonacci numbers.

**Solution:**
```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
```

### 94. Check for Anagram
**Problem:** Determine if two strings are anagrams.

**Solution:**
```python
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)
```

### 95. Flatten Nested List
**Problem:** Flatten a nested list using recursion.

**Solution:**
```python
def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result += flatten(i)
        else:
            result.append(i)
    return result
```

### 96. Find Duplicates in List
**Problem:** Return all duplicate elements in a list.

**Solution:**
```python
from collections import Counter

def find_duplicates(lst):
    return [item for item, count in Counter(lst).items() if count > 1]
```

### 97. Check Balanced Parentheses
**Problem:** Check if a string has balanced parentheses.

**Solution:**
```python
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
```

### 98. Prime Number Check
**Problem:** Determine if a number is a prime.

**Solution:**
```python
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
```

### 99. Top K Frequent Elements
**Problem:** Find the k most frequent elements in a list.

**Solution:**
```python
from collections import Counter

def top_k_frequent(nums, k):
    return [item for item, _ in Counter(nums).most_common(k)]
```

### 100. Reverse Words in String
**Problem:** Reverse the order of words in a string.

**Solution:**
```python
def reverse_words(s):
    return ' '.join(s.split()[::-1]
```

### 101. Check for Palindrome
**Problem:** Check if a string reads the same backward as forward.

**Solution:**
```python
def is_palindrome(s):
    return s == s[::-1]
```

### 102. Find the Missing Number
**Problem:** Find the missing number in a list of consecutive integers from 1 to n.

**Solution:**
```python
def missing_number(arr):
    n = len(arr) + 1
    return n * (n + 1) // 2 - sum(arr)
```

### 103. Fibonacci Generator
**Problem:** Generate the first n Fibonacci numbers.

**Solution:**
```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
```

### 104. Check for Anagram
**Problem:** Determine if two strings are anagrams.

**Solution:**
```python
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)
```

### 105. Flatten Nested List
**Problem:** Flatten a nested list using recursion.

**Solution:**
```python
def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result += flatten(i)
        else:
            result.append(i)
    return result
```

### 106. Find Duplicates in List
**Problem:** Return all duplicate elements in a list.

**Solution:**
```python
from collections import Counter

def find_duplicates(lst):
    return [item for item, count in Counter(lst).items() if count > 1]
```

### 107. Check Balanced Parentheses
**Problem:** Check if a string has balanced parentheses.

**Solution:**
```python
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
```

### 108. Prime Number Check
**Problem:** Determine if a number is a prime.

**Solution:**
```python
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
```

### 109. Top K Frequent Elements
**Problem:** Find the k most frequent elements in a list.

**Solution:**
```python
from collections import Counter

def top_k_frequent(nums, k):
    return [item for item, _ in Counter(nums).most_common(k)]
```

### 110. Reverse Words in String
**Problem:** Reverse the order of words in a string.

**Solution:**
```python
def reverse_words(s):
    return ' '.join(s.split()[::-1]
```

### 111. Check for Palindrome
**Problem:** Check if a string reads the same backward as forward.

**Solution:**
```python
def is_palindrome(s):
    return s == s[::-1]
```

### 112. Find the Missing Number
**Problem:** Find the missing number in a list of consecutive integers from 1 to n.

**Solution:**
```python
def missing_number(arr):
    n = len(arr) + 1
    return n * (n + 1) // 2 - sum(arr)
```

### 113. Fibonacci Generator
**Problem:** Generate the first n Fibonacci numbers.

**Solution:**
```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
```

### 114. Check for Anagram
**Problem:** Determine if two strings are anagrams.

**Solution:**
```python
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)
```

### 115. Flatten Nested List
**Problem:** Flatten a nested list using recursion.

**Solution:**
```python
def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result += flatten(i)
        else:
            result.append(i)
    return result
```

### 116. Find Duplicates in List
**Problem:** Return all duplicate elements in a list.

**Solution:**
```python
from collections import Counter

def find_duplicates(lst):
    return [item for item, count in Counter(lst).items() if count > 1]
```

### 117. Check Balanced Parentheses
**Problem:** Check if a string has balanced parentheses.

**Solution:**
```python
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
```

### 118. Prime Number Check
**Problem:** Determine if a number is a prime.

**Solution:**
```python
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
```

### 119. Top K Frequent Elements
**Problem:** Find the k most frequent elements in a list.

**Solution:**
```python
from collections import Counter

def top_k_frequent(nums, k):
    return [item for item, _ in Counter(nums).most_common(k)]
```

### 120. Reverse Words in String
**Problem:** Reverse the order of words in a string.

**Solution:**
```python
def reverse_words(s):
    return ' '.join(s.split()[::-1]
```

### 121. Check for Palindrome
**Problem:** Check if a string reads the same backward as forward.

**Solution:**
```python
def is_palindrome(s):
    return s == s[::-1]
```

### 122. Find the Missing Number
**Problem:** Find the missing number in a list of consecutive integers from 1 to n.

**Solution:**
```python
def missing_number(arr):
    n = len(arr) + 1
    return n * (n + 1) // 2 - sum(arr)
```

### 123. Fibonacci Generator
**Problem:** Generate the first n Fibonacci numbers.

**Solution:**
```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
```

### 124. Check for Anagram
**Problem:** Determine if two strings are anagrams.

**Solution:**
```python
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)
```

### 125. Flatten Nested List
**Problem:** Flatten a nested list using recursion.

**Solution:**
```python
def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result += flatten(i)
        else:
            result.append(i)
    return result
```

### 126. Find Duplicates in List
**Problem:** Return all duplicate elements in a list.

**Solution:**
```python
from collections import Counter

def find_duplicates(lst):
    return [item for item, count in Counter(lst).items() if count > 1]
```

### 127. Check Balanced Parentheses
**Problem:** Check if a string has balanced parentheses.

**Solution:**
```python
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
```

### 128. Prime Number Check
**Problem:** Determine if a number is a prime.

**Solution:**
```python
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
```

### 129. Top K Frequent Elements
**Problem:** Find the k most frequent elements in a list.

**Solution:**
```python
from collections import Counter

def top_k_frequent(nums, k):
    return [item for item, _ in Counter(nums).most_common(k)]
```

### 130. Reverse Words in String
**Problem:** Reverse the order of words in a string.

**Solution:**
```python
def reverse_words(s):
    return ' '.join(s.split()[::-1]
```

### 131. Check for Palindrome
**Problem:** Check if a string reads the same backward as forward.

**Solution:**
```python
def is_palindrome(s):
    return s == s[::-1]
```

### 132. Find the Missing Number
**Problem:** Find the missing number in a list of consecutive integers from 1 to n.

**Solution:**
```python
def missing_number(arr):
    n = len(arr) + 1
    return n * (n + 1) // 2 - sum(arr)
```

### 133. Fibonacci Generator
**Problem:** Generate the first n Fibonacci numbers.

**Solution:**
```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
```

### 134. Check for Anagram
**Problem:** Determine if two strings are anagrams.

**Solution:**
```python
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)
```

### 135. Flatten Nested List
**Problem:** Flatten a nested list using recursion.

**Solution:**
```python
def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result += flatten(i)
        else:
            result.append(i)
    return result
```

### 136. Find Duplicates in List
**Problem:** Return all duplicate elements in a list.

**Solution:**
```python
from collections import Counter

def find_duplicates(lst):
    return [item for item, count in Counter(lst).items() if count > 1]
```

### 137. Check Balanced Parentheses
**Problem:** Check if a string has balanced parentheses.

**Solution:**
```python
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
```

### 138. Prime Number Check
**Problem:** Determine if a number is a prime.

**Solution:**
```python
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
```

### 139. Top K Frequent Elements
**Problem:** Find the k most frequent elements in a list.

**Solution:**
```python
from collections import Counter

def top_k_frequent(nums, k):
    return [item for item, _ in Counter(nums).most_common(k)]
```

### 140. Reverse Words in String
**Problem:** Reverse the order of words in a string.

**Solution:**
```python
def reverse_words(s):
    return ' '.join(s.split()[::-1]
```

### 141. Check for Palindrome
**Problem:** Check if a string reads the same backward as forward.

**Solution:**
```python
def is_palindrome(s):
    return s == s[::-1]
```

### 142. Find the Missing Number
**Problem:** Find the missing number in a list of consecutive integers from 1 to n.

**Solution:**
```python
def missing_number(arr):
    n = len(arr) + 1
    return n * (n + 1) // 2 - sum(arr)
```

### 143. Fibonacci Generator
**Problem:** Generate the first n Fibonacci numbers.

**Solution:**
```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
```

### 144. Check for Anagram
**Problem:** Determine if two strings are anagrams.

**Solution:**
```python
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)
```

### 145. Flatten Nested List
**Problem:** Flatten a nested list using recursion.

**Solution:**
```python
def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result += flatten(i)
        else:
            result.append(i)
    return result
```

### 146. Find Duplicates in List
**Problem:** Return all duplicate elements in a list.

**Solution:**
```python
from collections import Counter

def find_duplicates(lst):
    return [item for item, count in Counter(lst).items() if count > 1]
```

### 147. Check Balanced Parentheses
**Problem:** Check if a string has balanced parentheses.

**Solution:**
```python
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
```

### 148. Prime Number Check
**Problem:** Determine if a number is a prime.

**Solution:**
```python
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
```

### 149. Top K Frequent Elements
**Problem:** Find the k most frequent elements in a list.

**Solution:**
```python
from collections import Counter

def top_k_frequent(nums, k):
    return [item for item, _ in Counter(nums).most_common(k)]
```

### 150. Reverse Words in String
**Problem:** Reverse the order of words in a string.

**Solution:**
```python
def reverse_words(s):
    return ' '.join(s.split()[::-1]
```
