from random import randint


def play_guess_game():
    number = randint(1, 10)
    guessed_number = 0

    while number != guessed_number:
        number = randint(1, 10)
        guessed_number =int(input("Guess your number" + "\n"))
        if(number == guessed_number):
           print (f"The correct number is {number} and your guess is {guessed_number}. Congrats! you won!")
        else:
            print( f"The correct number is {number} and your guess is {guessed_number}. Please try again" )


def main ():
    play_guess_game()

if __name__ == "__main__":
    main()