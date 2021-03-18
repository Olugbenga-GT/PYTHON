from random import randint


def play_guess_game():
    number = randint(1, 10)
    guessed_number = 0

    while number != guessed_number:
        number = randint(1, 10)
        try:
            guessed_number =int(input("Guess a number between 1 t0 10" + "\n"))
        except:
            print("Na number guesser game na! Guy enter number jare" + "\n")
        if(guessed_number < 1 or guessed_number > 10):
            print("Your number has to be between 1 and 10")
            break

        if(number == guessed_number):
           print (f"The correct number is {number} and your guess is {guessed_number}. Congrats! you won!")
        else:
            print( f"The correct number is {number} and your guess is {guessed_number}. Please try again" )


def main ():
    play_guess_game()

if __name__ == "__main__":
    main()