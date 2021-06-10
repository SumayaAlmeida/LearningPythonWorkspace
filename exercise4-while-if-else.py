import random

mistery_number = (random.randint(1,21))
no_of_guesses = 1
user_guess = 0

print("Let's play. I am thinking about a number.\n If you guess my number you win.") 

while user_guess != mistery_number:
    user_guess = int(input('Type a number between 1 and 20.\n'))
    
    

    if user_guess == mistery_number:
        print(f"you win. You have used {no_of_guesses} guesses")
        
    else:
        no_of_guesses +=1
        if user_guess < mistery_number:
            print("Higher. Try again")
        else:
            print("Lower. Try again")
    


#if user types anything else other than a number you should deal with that?
#number out of required range?
#