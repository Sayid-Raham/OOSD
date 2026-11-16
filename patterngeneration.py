n = int(input("Enter a positive integer: "))
 
if n <= 0:
    print("Please enter a positive number!")
else:
    print("\nNormal Pattern:")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()
 
    print("\nInverted Pattern:")
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end="")
        print()
 
    print("\nMultiplication Tables:")
    for i in range(1, n + 1):
        print("\nTable of", i)
        for j in range(1, 11):
            print(i, "x", j, "=", i * j)
