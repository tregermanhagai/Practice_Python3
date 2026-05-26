grades = [80, 90, 70, 60, 95, 55, 88, 92, 30, 82, 91, 87, 89, 94, 83, 86, 90, 80, 84, 88, 92]

count_passed_students = 0

for grade in grades:
    if grade >= 80:
        count_passed_students+=1

print(f"Number of students that passedd the exam from all the class:  {count_passed_students}/{len(grades)}")