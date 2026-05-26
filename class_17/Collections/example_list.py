
my_numbers = [5, 7, 2, 9, 1, "hello", 3.14, True]
my_numbers = [5, 7, 2, 9, 1, "hello", 3.14, True]
my_list = ["apple", "banana", "cherry", "apple", "avocado"]
text = "this_is_a_listz"
# print(my_list)

# for item in my_list:
#     if item.startswith('a'):
#         print(item)

# for item in my_numbers:
#         print(item)

# print (text[0])
# print (text[-1])

print(my_list)
my_list.append("orange")
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)
print("Number of items is my list: ", len(my_list))

list_len = len(my_list)
print("lenght of original list: ", len(my_list))
my_list.append(str(list_len))
list_len = len(my_list)
print("lenght of new list: ", len(my_list))

for item in my_list:
    print(item)

