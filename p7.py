from utils import spinnner_animation, time_function
import random
from itertools import combinations, product
import numpy as np
import secrets

def roll_dice() -> list[tuple[int, int]]:
    """Rolls 4 dice and returns all possible pairs of sums to choose from."""
    # Roll 4 dice using random
    #roll_sums = [random.randint(1, 6) for _ in range(4)]

    # Roll 4 dice, using numpy
    #roll_sums = np.random.randint(1,7,size = 4)
    
    # Roll 4 dice using sectrets
    roll_sums = [secrets.choice(range(1,7)) for  _ in range(4)]

    # Calculate all possible sums of two dice
    sums = [sum(pair) for pair in combinations(roll_sums, 2)]

    # Create sum pairs as per the cant stop game rules
    sum_pairs = [
        (sums[0], sums[5]),
        (sums[1], sums[4]),
        (sums[2], sums[3])
        ]
    return sum_pairs

@time_function
@spinnner_animation
def check_7s() -> None:

    loops = 1000000
    count_7s = 0
    for _ in range(loops):
        roll = roll_dice()
        is_even_in_roll = False
        for sum_pair in roll:
            if 7 in sum_pair:
                is_even_in_roll = True
        
        if is_even_in_roll:
            count_7s += 1
                
    print("\n")
    print("rolls with 7 percent: ", count_7s/loops)

check_7s()

def brute_force_check():
    all_rolls = list(product(range(1,7), repeat = 4))
    total_count = 0
    count_7s = 0

    for roll in all_rolls:
        sums = [sum(pair) for pair in combinations(roll,2)]
        sum_pairs = [
            (sums[0], sums[5]),
            (sums[1], sums[4]),
            (sums[2], sums[3])

        ]
        if any(7 in pair for pair in sum_pairs):
            count_7s += 1
        total_count += 1
    return count_7s/total_count

print("exact theoretial probability:", brute_force_check() )