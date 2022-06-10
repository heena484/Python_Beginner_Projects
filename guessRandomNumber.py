import random

def guess(range_of_random_number):
    random_number = random.randint(1,range_of_random_number)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess the Number between 1 and {range_of_random_number} : "))
        if random_number > guess:
            print("random number is lower")
        elif random_number < guess:
            print("random number is higher")
    print(f"Congragulations you have guessed the random number correctly {random_number}") 

 
guess(10)
