User = input('Enter  enter number ')

def append_User(lst, item):
    lst = [1,2, 3, 4, 5, 6, 7, 8,9, 11, 12 ]
    lst.append(item)
    return lst
print(append_User(list, 10))

def list_values():
    lst = []
    for i in range(5):
        num = int(input('enter values 1 to 12'  ))
        lst.append(num)
    for s in range(len(lst)):
        if lst[s] > 10:
            lst[s] = 10
    print(lst)

list_values()



#  How to return the length of a list?

# python
# Copy
# Edit
def get_length(lst):
    lst = [1, 2, 3, 4, 5]
    return len(lst)
print(get_length(list)) # Output: 5
# Q: Return the first element in a list.

# python
# Copy
# Edit


def first_element(lst):
    lst = [1, 2, 3, 4, 5]
    return lst[0]
print(first_element(list)) # Output: 1
# Q: Return the last element in a list.

# python
# Copy
# Edit
def last_element(lst):
    lst = [1, 2, 3, 4, 5]
    return lst[-1]
print(last_element(list)) # Output: 5
# Q: Return the sum of all elements.

# python
# Copy
# Edit
def sum_elements(lst):
    lst = [1, 2, 3, 4, 5]
    return sum(lst)
print(sum_elements(list)) # Output: 15
# Q: Check if a value exists in the list.

# python
# Copy
# Edit
def exists(lst, val):
    lst = [1, 2, 3, 4, 5]
    return val in lst
def extend_list(a, b):
    a.extend(b)
    return a

print(extend_list([1, 2, 3], [4, 5, 6]))  # Example usage
# Q: Return a sorted copy of the list.

# python
# Copy
# Edit
def sorted_list(lst):
    lst = [5, 3, 1, 4, 2]
    return sorted(lst)
print(sorted_list(list))
# Q: Return a reversed copy of the list.

# python
# Copy
# Edit
def reversed_list(lst):
    lst = [1, 2, 3, 4, 5]
    return lst[::-1]
print(reversed_list(list))
# Q: Append an item to the list.

# python
# Copy

def append_item(lst, item):
    lst = [1, 2, 3, 4, 5]
    lst.append(item)
    return lst
print(append_item(list, 6)) # Output: [1, 2, 3, 4, 5, 6]
# Q: Insert an item at a given index.

# python
# Copy
# Edit
def insert_item(lst, index, item):
    lst = [1, 2, 3, 4, 5]
    lst.insert(index, item)
    return lst
print(insert_item(list, 2, 10))
# Q: Remove an item by value.

# python
# Copy
# Edit
def remove_item(lst, item):
    lst = [1, 2, 3, 4, 5]
    lst.remove(item)
    return lst
print(remove_item(list, 3))
# Get the length of a list

# python
# Copy
# Edit
def get_length(lst):
    return len(lst)
# Get the first element

# python
# Copy
# Edit
def first_element(lst):
    return lst[0]
# Get the last element

# python
# Copy
# Edit
def last_element(lst):
    return lst[-1]
# Sum of all elements

# python
# Copy
# Edit
def sum_elements(lst):
    return sum(lst)
# Check if an element exists

# python
# Copy
# Edit
def exists(lst, val):
    return val in lst
# Sort a list

# python
# Copy
# Edit
def sorted_list(lst):
    return sorted(lst)
# Reverse a list

# python
# Copy
# Edit
def reversed_list(lst):
    return lst[::-1]
# Append an item

# python
# Copy
# Edit
def append_item(lst, item):
    lst.append(item)
    return lst
# Insert at index

# python
# Copy
# Edit
def insert_item(lst, index, item):
    lst.insert(index, item)
    return lst
# Remove by value

# python
# Copy
# Edit
def remove_item(lst, item):
    lst.remove(item)
    return lst
# 🔸 Indexing and Slicing
# Get a sublist from index 1 to 3

# python
# Copy
# Edit
def sublist(lst):
    return lst[1:4]
# Get every second element

# python
# Copy
# Edit
def every_second(lst):
    return lst[::2]
# Get elements in reverse order

# python
# Copy
# Edit
def reverse_elements(lst):
    return lst[::-1]
# Get the index of an element

# python
# Copy
# Edit
def get_index(lst, value):
    return lst.index(value)
# Count occurrences of an element

# python
# Copy
# Edit
def count_occurrences(lst, value):
    return lst.count(value)
# 🔸 List Math
# Find the maximum

# python
# Copy
# Edit
def get_max(lst):
    return max(lst)
# Find the minimum

# python
# Copy
# Edit
def get_min(lst):
    return min(lst)
# Calculate the average

# python
# Copy
# Edit
def average(lst):
    return sum(lst) / len(lst)
# Square all numbers

# python
# Copy
# Edit
def square_elements(lst):
    return [x**2 for x in lst]
# Filter even numbers

# python
# Copy
# Edit
def even_numbers(lst):
    return [x for x in lst if x % 2 == 0]
# 🔸 Transformations
# Convert all strings to uppercase

# python
# Copy
# Edit
def upper_case(lst):
    return [x.upper() for x in lst]
# Convert all to string

# python
# Copy
# Edit
def convert_to_string(lst):
    return [str(x) for x in lst]
# Concatenate strings in list

# python
# Copy
# Edit
def concat_strings(lst):
    return ''.join(lst)
# Remove empty strings

# python
# Copy
# Edit
def remove_empty(lst):
    return [x for x in lst if x]
# Multiply all numbers by 2

# python
# Copy
# Edit
def multiply_by_two(lst):
    return [x * 2 for x in lst]
# 🔸 Searching and Filtering
# Find first even number

# python
# Copy
# Edit
def first_even(lst):
    for x in lst:
        if x % 2 == 0:
            return x
    return None
# Return all numbers greater than 10

# python
# Copy
# Edit
def greater_than_ten(lst):
    return [x for x in lst if x > 10]
# Return elements that start with 'a'

# python
# Copy
# Edit
def starts_with_a(lst):
    return [x for x in lst if x.startswith('a')]
# Find duplicates

# python
# Copy
# Edit
def find_duplicates(lst):
    return [x for x in set(lst) if lst.count(x) > 1]
# Remove duplicates

# python
# Copy
# Edit
def remove_duplicates(lst):
    return list(dict.fromkeys(lst))
# 🔸 Advanced List Use
# Flatten a nested list

# python
# Copy
# Edit
def flatten(lst):
    return [item for sublist in lst for item in sublist]
# Zip two lists

# python
# Copy
# Edit
def zip_lists(a, b):
    return list(zip(a, b))
# Unzip a zipped list

# python
# Copy
# Edit
def unzip(lst):
    return list(zip(*lst))
# Find common elements

# python
# Copy
# Edit
def common_elements(a, b):
    return list(set(a) & set(b))
# Find difference between two lists

# python
# Copy
# Edit
def list_difference(a, b):
    return list(set(a) - set(b))
# 🔸 Using Loops and Conditions
# Sum using loop

# python
# Copy
# Edit
def sum_loop(lst):
    total = 0
    for num in lst:
        total += num
    return total
# Find the largest using loop

# python
# Copy
# Edit
def max_loop(lst):
    max_val = lst[0]
    for x in lst:
        if x > max_val:
            max_val = x
    return max_val
# Filter words longer than 4 letters

# python
# Copy
# Edit
def long_words(lst):
    return [x for x in lst if len(x) > 4]
# Check if all items are positive

# python
# Copy
# Edit
def all_positive(lst):
    return all(x > 0 for x in lst)
# Check if any item is negative

# python
# Copy
# Edit
def any_negative(lst):
    return any(x < 0 for x in lst)
# 🔸 List Manipulation
# Pop last item

# python
# Copy
# Edit
def pop_last(lst):
    lst.pop()
    return lst
# Pop item at index

# python
# Copy
# Edit
def pop_index(lst, idx):
    lst.pop(idx)
    return lst
# Extend list

# python
# Copy
# Edit
def extend_list(a, b):
    a.extend(b)
    return a
# Clear a list

# python
# Copy
# Edit
def clear_list(lst):
    lst.clear()
    return lst
# Copy a list

# python
# Copy
# Edit
def copy_list(lst):
    return lst.copy()
# 🔸 Miscellaneous
# Repeat list 3 times

# python
# Copy
# Edit
def repeat_list(lst):
    return lst * 3
# Convert list to set

# python
# Copy
# Edit
def to_set(lst):
    return set(lst)
# Check if list is empty

# python
# Copy
# Edit
def is_empty(lst):
    return len(lst) == 0
# Return unique sorted list

# python
# Copy
# Edit
def unique_sorted(lst):
    return sorted(set(lst))
# Join list with commas

# python
# Copy
# Edit
def join_with_commas(lst):
    return ','.join(lst)







# 🔹 Part 2: Python List Questions and Answers (51–100)
# 🔸 List Comprehensions & Filters
# Filter odd numbers

# python
# Copy
# Edit
def odd_numbers(lst):
    return [x for x in lst if x % 2 != 0]
# Filter numbers divisible by 5

# python
# Copy
# Edit
def divisible_by_five(lst):
    return [x for x in lst if x % 5 == 0]
# Get all uppercase words

# python
# Copy
# Edit
def uppercase_words(lst):
    return [x for x in lst if x.isupper()]
# Get all lowercase words

# python
# Copy
# Edit
def lowercase_words(lst):
    return [x for x in lst if x.islower()]
# Double even numbers

# python
# Copy
# Edit
def double_even(lst):
    return [x * 2 for x in lst if x % 2 == 0]
# 🔸 Functional Programming with Lists
# Use map to square numbers

# python
# Copy
# Edit
def map_square(lst):
    return list(map(lambda x: x**2, lst))
# Use filter to get positive numbers

# python
# Copy
# Edit
def filter_positive(lst):
    return list(filter(lambda x: x > 0, lst))
# Use reduce to multiply all elements

# python
# Copy
# Edit
from functools import reduce
def multiply_all(lst):
    return reduce(lambda x, y: x * y, lst)
# Use map to convert to strings

# python
# Copy
# Edit
def map_to_string(lst):
    return list(map(str, lst))
# Use filter to remove empty strings

# python
# Copy
# Edit
def remove_empty_strings(lst):
    return list(filter(None, lst))
# 🔸 Sorting and Custom Sorts
# Sort in descending order

# python
# Copy
# Edit
def sort_desc(lst):
    return sorted(lst, reverse=True)
# Sort by length of strings

# python
# Copy
# Edit
def sort_by_length(lst):
    return sorted(lst, key=len)
# Sort strings alphabetically ignoring case

# python
# Copy
# Edit
def sort_ignore_case(lst):
    return sorted(lst, key=str.lower)
# Sort list of tuples by second value

# python
# Copy
# Edit
def sort_by_second(lst):
    return sorted(lst, key=lambda x: x[1])
# Sort list of dicts by 'age'

# python
# Copy
# Edit
def sort_by_age(lst):
    return sorted(lst, key=lambda x: x['age'])
# 🔸 Combining and Splitting
# Merge two lists

# python
# Copy
# Edit
def merge_lists(a, b):
    return a + b
# Split list in half

# python
# Copy
# Edit
def split_half(lst):
    mid = len(lst) // 2
    return lst[:mid], lst[mid:]
# Interleave two lists

# python
# Copy
# Edit
def interleave_lists(a, b):
    return [val for pair in zip(a, b) for val in pair]
# Pair elements with their index

# python
# Copy
# Edit
def index_pairs(lst):
    return list(enumerate(lst))
# Chunk list into sublists of 3 elements

# python
# Copy
# Edit
def chunk_list(lst):
    return [lst[i:i+3] for i in range(0, len(lst), 3)]
# 🔸 Advanced Filtering & Searching
# Find first element matching condition

# python
# Copy
# Edit
def find_first_match(lst, func):
    for x in lst:
        if func(x):
            return x
    return None
# Get index of all even numbers

# python
# Copy
# Edit
def index_even(lst):
    return [i for i, x in enumerate(lst) if x % 2 == 0]
# Return list with duplicates removed, order preserved

# python
# Copy
# Edit
def remove_dupes(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]
# Check if all items are digits

# python
# Copy
# Edit
def all_digits(lst):
    return all(x.isdigit() for x in lst)
# Find most frequent item

# python
# Copy
# Edit
from collections import Counter
def most_common(lst):
    return Counter(lst).most_common(1)[0][0]
# 🔸 Nested List Tasks
# Count total elements in nested list

# python
# Copy
# Edit
def count_nested(lst):
    return sum(len(sub) for sub in lst)
# Find max in each sublist

# python
# Copy
# Edit
def max_each_sublist(lst):
    return [max(sub) for sub in lst]
# Transpose 2D matrix

# python
# Copy
# Edit
def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))
# Flatten 3D list to 1D

# python
# Copy
# Edit
def flatten_3d(lst):
    return [x for sub1 in lst for sub2 in sub1 for x in sub2]
# Find row with max sum

# python
# Copy
# Edit
def max_row_sum(matrix):
    return max(matrix, key=sum)
# 🔸 Boolean Checks and Utilities
# Are all elements equal?

# python
# Copy
# Edit
def all_equal(lst):
    return lst.count(lst[0]) == len(lst)
# Is list strictly increasing?

# python
# Copy
# Edit
def strictly_increasing(lst):
    return all(x < y for x, y in zip(lst, lst[1:]))
# Is list a palindrome?

# python
# Copy
# Edit
def is_palindrome(lst):
    return lst == lst[::-1]
# Are two lists equal ignoring order?

# python
# Copy
# Edit
def equal_ignore_order(a, b):
    return sorted(a) == sorted(b)
# Are there any duplicates?

# python
# Copy
# Edit
def has_duplicates(lst):
    return len(lst) != len(set(lst))
# 🔸 Miscellaneous Logic
# Sum of odd indexed elements

# python
# Copy
# Edit
def sum_odd_indices(lst):
    return sum(lst[1::2])
# Difference between max and min

# python
# Copy
# Edit
def range_of_list(lst):
    return max(lst) - min(lst)
# Count elements greater than average

# python
# Copy
# Edit
def above_avg(lst):
    avg = sum(lst) / len(lst)
    return sum(1 for x in lst if x > avg)
# Reverse in place

# python
# Copy
# Edit
def reverse_in_place(lst):
    lst.reverse()
    return lst
# Swap first and last

# python
# Copy
# Edit
def swap_first_last(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst
# 🔸 String + List Interactions
# Convert sentence to list of words

# python
# Copy
# Edit
def split_words(sentence):
    return sentence.split()
# Convert list of words to sentence

# python
# Copy
# Edit
def join_words(lst):
    return ' '.join(lst)
# Filter numeric strings

# python
# Copy
# Edit
def filter_numbers(lst):
    return [x for x in lst if x.isdigit()]
# Capitalize all strings

# python
# Copy
# Edit
def capitalize_list(lst):
    return [x.capitalize() for x in lst]
# Get lengths of each string

# python
# Copy
# Edit
def lengths(lst):
    return [len(x) for x in lst]
# 🔸 Custom Utilities
# Pad list with zeros to length 5

# python
# Copy
# Edit
def pad_zeros(lst):
    return lst + [0] * (5 - len(lst))
# Remove all None values

# python
# Copy
# Edit
def remove_none(lst):
    return [x for x in lst if x is not None]
# Get elements at prime indexes

# python
# Copy
# Edit
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

def prime_index_elements(lst):
    return [lst[i] for i in range(len(lst)) if is_prime(i)]
# Find first duplicate

# python
# Copy
# Edit
def first_duplicate(lst):
    seen = set()
    for x in lst:
        if x in seen:
            return x
        seen.add(x)
    return None
# Repeat each element twice

# python
# Copy
# Edit
def repeat_twice(lst):
    return [x for item in lst for x in (item, item)]








# Square only even numbers

# python
# Copy
# Edit
def square_evens(lst):
    return [x**2 for x in lst if x % 2 == 0]
# Cube only odd numbers

# python
# Copy
# Edit
def cube_odds(lst):
    return [x**3 for x in lst if x % 2 != 0]
# Apply different function for even/odd

# python
# Copy
# Edit
def conditional_transform(lst):
    return [x**2 if x % 2 == 0 else x**3 for x in lst]
# Multiply corresponding items in two lists

# python
# Copy
# Edit
def elementwise_multiply(a, b):
    return [x * y for x, y in zip(a, b)]
# Divide corresponding items with rounding

# python
# Copy
# Edit
def divide_and_round(a, b):
    return [round(x / y, 2) for x, y in zip(a, b) if y != 0]
# 🔸 Advanced Checks
# Are all elements positive?

# python
# Copy
# Edit
def all_positive(lst):
    return all(x > 0 for x in lst)
# Is list sorted ascending?

# python
# Copy
# Edit
def is_sorted(lst):
    return lst == sorted(lst)
# Is list sorted descending?

# python
# Copy
# Edit
def is_sorted_desc(lst):
    return lst == sorted(lst, reverse=True)
# Are all strings alphanumeric?

# python
# Copy
# Edit
def all_alnum(lst):
    return all(x.isalnum() for x in lst)
# Check if two lists are permutations

# python
# Copy
# Edit
def are_permutations(a, b):
    return sorted(a) == sorted(b)
# 🔸 Set Operations with Lists
# Get common elements

# python
# Copy
# Edit
def intersection(a, b):
    return list(set(a) & set(b))
# Get unique elements in both lists

# python
# Copy
# Edit
def union_unique(a, b):
    return list(set(a) | set(b))
# Get items only in first list

# python
# Copy
# Edit
def difference(a, b):
    return list(set(a) - set(b))
# Symmetric difference (exclusive to each list)

# python
# Copy
# Edit
def symmetric_diff(a, b):
    return list(set(a) ^ set(b))
# Remove duplicates while preserving order

# python
# Copy
# Edit
def dedup(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]
# 🔸 More Nested List Handling
# Sum each sublist

# python
# Copy
# Edit
def sum_sublists(lst):
    return [sum(sub) for sub in lst]
# Flatten nested list one level

# python
# Copy
# Edit
def flatten_once(lst):
    return [item for sublist in lst for item in sublist]
# Find sublist with max average

# python
# Copy
# Edit
def max_avg_sublist(lst):
    return max(lst, key=lambda x: sum(x)/len(x))
# Filter sublists with even sum

# python
# Copy
# Edit
def even_sum_sublists(lst):
    return [sub for sub in lst if sum(sub) % 2 == 0]
# Count total odd numbers in 2D list

# python
# Copy
# Edit
def count_odds(lst):
    return sum(1 for row in lst for x in row if x % 2 != 0)
# 🔸 List + Dict Interactions
# Convert list to dict with index as key

# python
# Copy
# Edit
def list_to_dict(lst):
    return {i: val for i, val in enumerate(lst)}
# Convert dict values to list

# python
# Copy
# Edit
def dict_values_to_list(d):
    return list(d.values())
# List of dicts → list of names

# python
# Copy
# Edit
def extract_names(lst):
    return [d['name'] for d in lst if 'name' in d]
# Filter list of dicts by key value

# python
# Copy
# Edit
def filter_by_age(lst, min_age):
    return [d for d in lst if d.get('age', 0) >= min_age]
# Count occurrences of value in dict list

# python
# Copy
# Edit
def count_status(lst, status):
    return sum(1 for d in lst if d.get('status') == status)
# 🔸 Searching & Indexing
# Find index of max element

# python
# Copy
# Edit
def index_of_max(lst):
    return lst.index(max(lst))
# Find index of min element

# python
# Copy
# Edit
def index_of_min(lst):
    return lst.index(min(lst))
# Find all indexes of value

# python
# Copy
# Edit
def find_all_indexes(lst, value):
    return [i for i, x in enumerate(lst) if x == value]
# Get values above threshold

# python
# Copy
# Edit
def above_threshold(lst, t):
    return [x for x in lst if x > t]
# Get first element greater than 100

# python
# Copy
# Edit
def first_gt_100(lst):
    return next((x for x in lst if x > 100), None)
# 🔸 Real-World List Tasks
# Extract email usernames

# python
# Copy
# Edit
def email_usernames(lst):
    return [email.split('@')[0] for email in lst]
# Mask all but last 4 digits in list of phone numbers

# python
# Copy
# Edit
def mask_phones(lst):
    return ['****' + num[-4:] for num in lst]
# Check if any element is a URL

# python
# Copy
# Edit
def has_url(lst):
    return any(x.startswith('http') for x in lst)
# Filter out spam words

# python
# Copy
# Edit
def filter_spam(lst, spam_words):
    return [x for x in lst if not any(spam in x for spam in spam_words)]
# Summarize product prices

# python
# Copy
# Edit
def total_price(products):
    return sum(p['price'] for p in products)
# 🔸 List Logic Games
# Check Tic-Tac-Toe win

# python
# Copy
# Edit
def check_win(board, symbol):
    return any(all(cell == symbol for cell in row) for row in board)
# Generate a list of random integers

# python
# Copy
# Edit
import random
def random_list(n, start, end):
    return [random.randint(start, end) for _ in range(n)]
# Rotate list left by 1

# python
# Copy
# Edit
def rotate_left(lst):
    return lst[1:] + lst[:1]
# Rotate list right by 1

# python
# Copy
# Edit
def rotate_right(lst):
    return lst[-1:] + lst[:-1]
# Find median of list

# python
# Copy
# Edit
def median(lst):
    lst = sorted(lst)
    n = len(lst)
    mid = n // 2
    return (lst[mid] + lst[~mid]) / 2
# 🔸 Final 10 — Practice Utilities
# Find mode of list

# python
# Copy
# Edit
from statistics import mode
def find_mode(lst):
    return mode(lst)
# Get running total of list

# python
# Copy
# Edit
def running_total(lst):
    total = 0
    result = []
    for x in lst:
        total += x
        result.append(total)
    return result
# Count how many are True

# python
# Copy
# Edit
def count_true(lst):
    return sum(1 for x in lst if x is True)
# Remove punctuation from strings

# python
# Copy
# Edit
import string
def clean_strings(lst):
    return [x.translate(str.maketrans('', '', string.punctuation)) for x in lst]
# Check if any string is palindrome

# python
# Copy
# Edit
def has_palindrome(lst):
    return any(s == s[::-1] for s in lst)
# Sum all digits in list of strings

# python
# Copy
# Edit
def sum_digits(lst):
    return sum(int(ch) for s in lst for ch in s if ch.isdigit())
# Filter strings with only letters

# python
# Copy
# Edit
def only_letters(lst):
    return [x for x in lst if x.isalpha()]
# Replace negative numbers with 0

# python
# Copy
# Edit
def replace_negatives(lst):
    return [0 if x < 0 else x for x in lst]
# Convert strings to lowercase

# python
# Copy
# Edit
def lowercase_all(lst):
    return [x.lower() for x in lst]
# Round all floats in list

# python
# Copy
# Edit
def round_floats(lst):
    return [round(x) for x in lst if isinstance(x, float)]


