from random import randint


def get_number():
    while True:
        try:
            user_pick = int(input("Enter your number: "))
            return user_pick
        except ValueError:
            print("It's not a number! Pick a number.")
    return user_pick


def get_hint():
    hints = ['too small', 'too big', 'you won']
    while True:
        hint = input('Hint: ').lower()
        if hint in hints:
            break
        print(f"Hint is not in {hints}")
    return hint


def pc_guess():
    goal = get_number()
    min_value = 0
    max_value = 1000
    tries = 0
    hint = get_hint()
    while hint != 'you won' or tries == 10:
        guessed = (max_value - min_value) / 2 + min_value
        print(f'I chose: {guessed}')
        hint = get_hint()
        if hint == 'too big':
            max_value = guessed
            tries += 10
        elif hint == 'too small':
            min_value = guessed
            tries += 10

    print("Ha! I won!")

print("Choose a number between 0 and 1000 and I'll try to guess it. I have only 10 tries.\n")

pc_guess()
