import random

highest = 10
answer = random.randint(1, highest)
guess = 0
print("Please guess a number between 1 and {}. You can press 0 to exit.: ".format(highest))

while guess != answer:
    guess = int(input())

    if guess == 0:      # To exit the game.
        break
    elif guess == answer:
        print("You got it right.")
        
    else:
        if guess < answer:
            print("Please guess higher.")
        else:
            print("Please guess lower.")