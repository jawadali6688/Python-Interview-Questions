# What is the difference between mutable and immutable data
# types? (Explain with coding example)

# String example --> immutable 

# my_str = "Jawad"

# print(f"Orignal memory ref: {id(my_str)}")

# my_str += "Khan"

# print(f"New memory ref: {id(my_str)}")


# my_list = [1, 4, 5]

# print(f"Orignal memory ref: {id(my_list)}")

# my_list.append(7)

# print(f"New memory ref: {id(my_list)}")



# What is type conversion? How is it done in Python

# Data Type --> Changing 

# num1 = 5

# num2 = 5.5

# num3 = num1 + num2

# print(type(num3))

# print(type(int(num3)))

# my_list = [3, 5, 5, 7, 7, 7, 9]

# new_list = list(set(my_list))

# print(new_list)


# What is the purpose of the None type in Python?

# my_type = None

# def test_func(name=None):

#     if name:
#         print("Yes your name is ", name)
#     elif not name:
#         print("No name 1")
#     else:
#         print("No name2 ")

# test_func()


# How is memory allocated for different data types in Python?

# Mutable --> dynamic memory 

# Immutable --> not changeable memory

# import sys
# my_str = "Jawad"

# my_list = [1, 4, 5]

# print("Memory for string", sys.getsizeof(my_str), "KB")

# my_str += "Ali KHan"

# print("Memory for string", sys.getsizeof(my_str), "KB")

# print("Memory for list", sys.getsizeof(my_list), "KB")
# my_list.append(10)

# print("Memory for list", sys.getsizeof(my_list), "KB")


# How do Python’s built-in functions type() and id() work?

my_str = "Jawad"

print(f"Type function tell us type {type(my_str)}")

print(f"id function tell memory reference {id(my_str)}")

