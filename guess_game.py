from random import randint
random_number = randint(0,10)
guessednumber = int(input("Guess the number "))
while guessednumber != random_number:
    if guessednumber > random_number:
        print("Too High! Guess again.\n")
        guessednumber
    elif guessednumber < random_number:
        print("Too Low! Guess again.\n")
        guessednumber
    elif guessednumber == random_number:
        print("Well done! The number is " + random_number)
        break
