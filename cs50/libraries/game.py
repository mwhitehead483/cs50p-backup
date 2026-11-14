import random

def get_level():
    while(True):
        try:
            level = input("Level: ")
            if level.isdigit() and int(level) > 0:
                return level
        except ValueError:
            pass

def guess():
    # must be numeric
    level = int(get_level())
    random_number = random.randint(1, level)
    while(True):
        try:
            guess = input("Guess: ")
            if guess.isdigit() and int(guess) > 0:
                if int(guess)  == random_number:
                    print("Just right!" )
                    break;
                if int(guess) < random_number:
                    print("Too small!")
                else:
                    print("Too large!")
        except ValueError:
            pass

def main():
    guess()

if __name__ == "__main__":
    main()
