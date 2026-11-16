balance = 50000
 
while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
 
    choice = int(input("Enter your choice: "))
 
    if choice == 1:
        print("Your Balance is Rs.", balance)
 
    elif choice == 2:
        amount = int(input("Enter deposit amount: "))
 
        if amount <= 0:
            print("Invalid deposit amount!")
        else:
            balance += amount
            print("Money deposited successfully!")
            print("New Balance:", balance)
 
    elif choice == 3:
        amount = int(input("Enter withdrawal amount: "))
 
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif amount > balance:
            print("Insufficient Balance!")
        else:
            balance -= amount
            print("Withdrawal successful!")
            print("Remaining Balance:", balance)
 
    elif choice == 4:
        print("Thank you for using ATM!")
        break
 
    else:
        print("Invalid choice!")
