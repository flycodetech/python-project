def create_list():
    fruits = ["apple", "banana", "cherry"]
    fruits.append("orange")
    return fruits

my_list = create_list()
print("List:", my_list)
#  Explanation: A list is mutable. We use append() to add an element.


# Tuple Example in a Function
# python

def create_tuple():
    coordinates = (10, 20)
    return coordinates

my_tuple = create_tuple()
print("Tuple:", my_tuple)
# Explanation: A tuple is immutable. It’s often used for fixed collections of items.

#  Dictionary Example in a Function
# python

def create_dict():
    student = {"name": "Alice", "age": 20, "grade": "A"}
    student["age"] = 21  # Updating a value
    return student

my_dict = create_dict()
print("Dictionary:", my_dict)