import random

def get_level():
    # must be numeric
    while (True):
        level = input("Level: ")
        if level.isdigit() and int(level) in (1, 2, 3):
            return int(level)

def generate_integer(level):
    # allow only 1,2,3, use random...
    random_number = 0
    if level == 1:
        random_number = random.randint(0, 9)
    elif level == 2:
        random_number = random.randint(10, 99)
    elif level == 3:
        random_number = random.randint(100, 999)
    return random_number


def doProblemSet(level):
    score = 0

    for _ in range(10):  # Loops 10 times for the 10 problems
        # X, Y = generate_integer(level)

        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        # Track errors for this specific problem (up to 3 tries)
        error_count = 0
        while error_count < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == correct_answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    error_count += 1
            except ValueError:
                print("EEE")
                error_count += 1

        # If they failed 3 times, show the correct answer
        if error_count == 3:
            print(f"{x} + {y} = {correct_answer}")

    print(f"Score: {score}")



def main():
    # get a level - 1 digit number, 2 digit, 3 digit
    # repeat 10 times.
    # get x and y and add
    # prompt user for correct answer
    # check if answer is correct.

    score = 0
    level = get_level()



    score = doProblemSet(int(level))

    #print(f"Score: {score}")


if __name__ == "__main__":
    main()


