correct_username = "admin"
correct_password = "12345"
 
attempts = 3
 
while attempts > 0:
    username = input("Enter Username: ")
    password = input("Enter Password: ")
 
    if username == "" or password == "":
        print("Username and password cannot be empty!")
        attempts -= 1
        print("Attempts Remaining:", attempts)
 
    elif username == correct_username and password == correct_password:
        print("Login Successful!")
        break
 
    else:
        attempts -= 1
        print("Incorrect Username or Password!")
        print("Attempts Remaining:", attempts)
 
else:
    print("Account Locked!")
