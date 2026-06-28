import random

target = random.randint(1, 100)

print("I am thinking of a number between 1 and 100.")

while True:
    try:
        guess = int(input("Enter your guess: "))
        
        if guess < target:
            print("Too low! Try again.")
        elif guess > target:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed it!")
            break
            
    except ValueError:
        print("Please enter a valid number.")
