even = 0
odd = 0
total = 0
count = 0
largest = None
 
while True:
    num = int(input("Enter an integer (0 to stop): "))
 
    if num == 0:
        break
 
    if num < 0:
        print("Negative number ignored!")
        continue
 
    if num % 2 == 0:
        print("Even Number")
        even += 1
    else:
        print("Odd Number")
        odd += 1
 
    total += num
    count += 1
 
    if largest is None or num > largest:
        largest = num
 
print("\n--- Number Analysis Report ---")
print("Even Numbers:", even)
print("Odd Numbers:", odd)
 
if count > 0:
    average = total / count
    print("Largest Number:", largest)
    print("Sum:", total)
    print("Average:", average)
else:
    print("No positive numbers were entered.")
