### 2. Find the Missing Number
# **Problem:** Find the missing number in a list of consecutive integers from 1 to n.

# **Solution:**
# ```python
def missing_number(arr):
    n = len(arr) + 1
    return n * (n + 1) // 2 - sum(arr)
# ```
print(missing_number([12, 15,20, 30]))
