# Positional arguments
# def add(p1, p2):
#     return p1 + p2
#
#
# print(add(3, 5))
#
# # You can also specify the parameters if you wish (keyword arguments).
# print(add(3, p2=5))
# # print(add(p1=3, 5))  # Error: positional arguments must be specified first
# print(add(p1=3, p2=5))
# print(add(p2=5, p1=3))


# =================================================================================


# # # Positional arguments with default parameter values
# def add(p1, p2=10):
#     return p1 + p2
#
#
# print(add(3))  # p2 is optional because it has a default value
# print(add(3, 5))


# etc. as above

# def add(p1=5, p2):  # Error: non-default parameters must be specified first
#     return p1 + p2
#
# # =================================================================================
#
#
# # *args accepts positional arguments as a tuple (doesn't have to be called *args)
# def add_all(*args):  # The * packs the positional arguments into a tuple
#     print(f'{args = }')
#     total = 0
#     for number in args:
#         print(f'Adding {number}')
#         total += number
#     return total


# print(add_all(1, 2, 3, 4, 5))
# my_list = [2, 5, 6, 7, 10]
# print(add_all(*my_list))  # The * unpacks the list into positional arguments
#
#
# # =================================================================================
#
#
# **kwargs accepts positional arguments as a dictionary (doesn't have to be called **kwargs)
def add_all(**kwargs):  # The ** packs the keyword arguments into a dictionary
    print(f'{kwargs = }')
    total = 0
    for key, value in kwargs.items():
        print(f'Adding {key}: {value}')
        total += value
    return total


print(add_all(a=1, d=4, c=3, e=5, b=2))
my_dict = {'a': 1, 'd': 4, 'c': 3, 'e': 5, 'b': 2}
print(add_all(**my_dict))  # The ** unpacks the dictionary into keyword arguments