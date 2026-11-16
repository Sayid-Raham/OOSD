import random
 
secret_number = random.randint(1, 100)
attempts = 0
 
while attempts < 7:
    guess = int(input("Guess a number (1-100): "))
 
    if guess < 1 or guess > 100:
        print("Invalid! Enter number between 1 and 100.")
        continue
 
    attempts += 1
 
    if guess == secret_number:
        print("Congratulations! You guessed correctly!")
 
        if attempts == 1:
            print("Perfect Score!")
        else:
            print("Attempts Used:", attempts)
 
        break
 
    elif guess < secret_number:
        print("Secret number is HIGHER!")
    else:
        print("Secret number is LOWER!")
 
else:
    print("Game Over!")
    print("Secret Number was:", secret_number)
