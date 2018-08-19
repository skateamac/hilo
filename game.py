import random


def main():
    print("Welcome to the HI - LO game")
    guessed_it = False
    num = random.randint(1, 100)
    while not guessed_it:
        guessed_it = guess(num)


def guess(num):
    user_guess = int(input("Guess a number between 1 & 100: "))
    guessed_it = False
    if user_guess > num:
        print("Too high!")
        return False
    elif user_guess < num:
        print("Too low!")
    else:
        print("Got it: The number is {}".format(num))
        guessed_it = True
    return guessed_it


if __name__ == '__main__':
    main()
