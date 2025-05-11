### 3. Fibonacci Generator
# **Problem:** Generate the first n Fibonacci numbers.

# **Solution:**
# ```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
# ```
print(fibonacci(20))