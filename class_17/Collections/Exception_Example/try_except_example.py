# my_list = [1, 6, 8]

# try:
#     print(my_list[3])
# except:
#     print("error")
    

try:
    result = 10 / a0
except ZeroDivisionError:
    print("error")
except Exception as e:
    print("An error occurred:", str(e))