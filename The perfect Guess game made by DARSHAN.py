import random
randNumber = random.randint(1, 100)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess =int(input("Enter youre guess: "))
    guesses += 1
    if(userGuess==randNumber):
        print("You gussed it right!")
    else:
        if(userGuess>randNumber):
            print("You gussed it wrong!Enter a smaller Number")
        else:
            print("You gueesed it wrong!Enter a larger number")
            
print(f"You guessed the number in {guesses}guesses")
with open("hiscore.txt","w")as f:
    f.write(str(guesses))