import random

def roll_four_dice() -> tuple[int, int, int, int]:
    """
    Rolls four six-sided dice and returns the results.

    Returns:
        tuple[int, int, int, int]: A tuple representing the result of each die roll (1-6).
    """
    roll_results = tuple(random.randint(1, 6) for _ in range(4))
    return roll_results

def roll_sum_options(roll: tuple[int, int, int, int]) -> list[tuple[int, int]]:
    """
    Calculate three specific pairs of sum options based on the roll.

    Args:
        roll (tuple[int, int, int, int]): A tuple representing the results of the dice rolls.

    Returns:
        list[tuple[int, int]]: A list of three tuples where each tuple represents two sums.
    """
    # Calculate the three specific pairs of sums
    sum_options = [
        (roll[0] + roll[1], roll[2] + roll[3]),  # Pair 1: sum of dice 1 + 2 and 3 + 4
        (roll[0] + roll[2], roll[1] + roll[3]),  # Pair 2: sum of dice 1 + 3 and 2 + 4
        (roll[0] + roll[3], roll[1] + roll[2])   # Pair 3: sum of dice 1 + 4 and 2 + 3
    ]

    return sum_options

# Example Usage
if __name__ == "__main__":
    # Roll four dice
    dice_rolls = roll_four_dice()
    print(f"Rolling four dice: {dice_rolls}")

    # Calculate sum pairs options
    sum_options = roll_sum_options(dice_rolls)
    print(f"Unique sum options (pairs): {sum_options}")
