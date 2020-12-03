import random
import time as t
number = random.randint(1, 25) # random generate
guess = int(input("What is the Number: "))
while guess != number:
    if guess > number:
        print("Guess Lower")
        guess = int(input("What is the Number: "))
    if guess < number:
        print("Guess Higher")
        guess = int(input("What is the Number: "))   
if guess == number:
    print("Correct!")
    print('This window will close in 3 seconds')
    t.sleep(3)
    
        
