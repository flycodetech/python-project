# this is a common interview question.

# Problem Understanding:
# A palindrome is a number that reads the same forward and backward.

# For example:

# 121 is a palindrome

# -121 is not (because of the negative sign)

# 10 is not (reverse is 01)

# Solution 1: Using String Conversion (Easy)
# python

def isPalindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]
      
# But the follow-up asks for a solution without converting the integer to a string.

# Solution 2: Without String Conversion (Efficient)
# We reverse half of the number and compare it with the other half.

# python

def isPalindrome(x: int) -> bool:
    # Negative numbers and numbers ending with 0 (but not 0 itself) are not palindromes
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10

    # For even digits: x == reversed_half
    # For odd digits: x == reversed_half // 10 (middle digit doesn't matter)
    return x == reversed_half or x == reversed_half // 10
# 🔍 Example Walkthrough: x = 1221
# Iteration 1: reversed_half = 1, x = 122

# Iteration 2: reversed_half = 12, x = 12

# Now x == reversed_half → it's a palindrome 

# ⏱ Time Complexity:
# O(log₁₀(x)) — because we are dividing x by 10 each iteration

# 📦 Space Complexity: