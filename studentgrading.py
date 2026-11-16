marks_list = []
passed = 0
failed = 0
 
for i in range(1, 11):
    while True:
        marks = int(input(f"Enter marks of student {i}: "))
 
        if marks < 0 or marks > 100:
            print("Invalid marks! Enter between 0 and 100.")
            continue
        else:
            break
 
    marks_list.append(marks)
 
    if marks >= 50:
        passed += 1
    else:
        failed += 1
 
    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    elif marks >= 60:
        grade = "D"
    else:
        grade = "F"
 
    print("Grade:", grade)
 
highest = max(marks_list)
average = sum(marks_list) / 10
 
print("\n--- Class Result ---")
print("Passed Students:", passed)
print("Failed Students:", failed)
print("Highest Marks:", highest)
print("Class Average:", average)
