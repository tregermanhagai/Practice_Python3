def count_char_in_string(text='test text', char='a'):
    """function count the number of appearnces of char in a string"""
    count = text.count(char)
    return count


count = count_char_in_string()
print(count)

text = input("Type a string: ")
char = input("Type a char to search in the string (default is 'a'): ") or 'a'
count = count_char_in_string(text, char)
print("Letter appear: ", count)