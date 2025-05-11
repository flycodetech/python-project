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

# def two_sum(num, terget):
#     lookup ={}
#     for i, num in enumerate(nums):
#         if terget - num in lookup:
#             return [lookup[terget - num], i]
#         lookup[num] = i 