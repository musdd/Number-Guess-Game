import random

# Gets the number for numRange and numOfGuess and checks if they are integers or not before returning the value
def getNumber():
    try:
        numRange = int(input("Number of range: "))
        numOfGuess = int(input("Number of Guesses: "))
    except ValueError:
        pass
    else:
        return (numRange, numOfGuess)
    
def main():
    numRange, numOfGuess = getNumber()
    number = random.randint(1, numRange)
    guesses = 0
    while guesses < numOfGuess:

    #  While guesses is less than numOfGuess, continue the code. If the guesses becomes equal or greater than, 
    #  then it will return false and stop the loop
        try:
            choose = int(input("Choose a number: "))
        except ValueError:
            pass
        else:
            guesses += 1
            
            # simple if-else to know whether the number inputted is equal or not to the random number.
            if choose > number:
                print(f"Too High. You have {numOfGuess - guesses} tries remaining")
            elif choose < number:
                print(f"Too Low. You have {numOfGuess - guesses} tries remaining")
            else:
                print(f"You won! it took you a grand total of {guesses} guesses to get it.")
                return False

    # if the loop finished looping, and still not broken, this part is executed.
    else: 
        print(f"You lost, I was thinking of {number}")
        tryAgain = (input("Try again?\n1.Yes\n2.No\n")).strip().lower()
        if tryAgain in {"1", "yes"}:
            main()
        else:
            SystemExit

print("Welcome to Guess the number!")
main()
