n = int(input("Enter number of terms: "))
 
if n < 1:
    print("Please enter at least 1 term!")
else:
    a = 0
    b = 1
    total = 0
    even = 0
    odd = 0
 
    print("Fibonacci Sequence:")
 
    for i in range(n):
        print(a, end=" ")
        total += a
 
        if a % 2 == 0:
            even += 1
        else:
            odd += 1
 
        a, b = b, a + b
 
    print("\nSum:", total)
    print("Even terms:", even)
    print("Odd terms:", odd)
