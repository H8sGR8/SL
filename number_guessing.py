from random import randint
lowest = int()
highest = int()
is_number = 0
while is_number == 0:
    try:
        lowest = int(input("give the lowest number\n"))
        is_number = 1
    except ValueError:
        print("its not a number")
is_number = 0
while is_number == 0:
    try:
        highest = int(input("give the highest number\n"))
        is_number = 1
        if highest < lowest:
            print("highest must be bigger than lowest")
            is_number = 0
    except ValueError:
        print("its not a number")
guess = int()
num_of_guesses = 0
r_number = randint(lowest, highest)
while guess != r_number:
    is_number = 0
    while is_number == 0:
        try:
            guess = int(input("guess number\n"))
            is_number = 1
            num_of_guesses += 1
        except ValueError:
            print("its not a number")
    if guess < r_number:
        print("higher")
    elif guess > r_number:
        print("lower")
    else:
        print("you guessed the number in " + str(num_of_guesses) + " guesses")
