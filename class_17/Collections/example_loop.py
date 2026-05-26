search_name = "asi"
students = ["moshe", "asi", "rami", "dana", "yossi"]
is_exist = False

for s in students:
    if search_name in s:
        is_exist = True
        break


print("The student is exist: ", search_name, is_exist)
    
