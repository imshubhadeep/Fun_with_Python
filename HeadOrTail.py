import random # Import random module.

guess = int(input("Enter 'HEAD(1)'/ 'TAIL(0)' : "))

# rand = random.seed(guess)
random_side = random.randint(0,1) #Find random value between 0 and 1.

if guess == random_side:
    print("Congraculations! You Win the TOSS.")
else:
    print("Sorry! You lose the TOSS.")