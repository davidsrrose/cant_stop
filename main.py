from game import cant_stop_game


def roll() -> list[tuple[int, int]]:
    """Rolls 4 dice and returns all possible pairs of sums to choose from."""
    # Simulated dice rolls
    roll_results = [3, 4, 1, 3]

    # Calculate all possible sums of two dice
    sums = [sum(pair) for pair in combinations(roll_results, 2)]

    # Create sum pairs as per the game's logic
    sum_pairs = [(sums[0], sums[5]), (sums[1], sums[4]), (sums[2], sums[3])]

    return sum_pairs

def roll(self) -> list[tuple[int, int]]:
    """Rolls 4 dice and returns all possible pairs of sums to choose from."""
    # Roll 4 dice
    roll_results = [random.randint(1, 6) for _ in range(4)]
    print(f"Rolled dice: {roll_results}")

    # Calculate all possible sums of two dice
    sums = [sum(pair) for pair in combinations(roll_results, 2)]

    # Create sum pairs as per the game's logic
    sum_pairs = [(sums[0], sums[5]), (sums[1], sums[4]), (sums[2], sums[3])]
    return sum_pairs

def choose_sums(game_state, sums) -> list[int]:
    """ Function to choose which sums/ lane on we want to advance on """


    pass

def single_game():
    """  Plays one single game of solitaire cant_stop """

    # initilize game
    game = cant_stop_game.__init__()
    # Roll dice

    # Check game for terninal state
    if terminate_game:
        return False
    

    # Pick Sums

    return True
    

def main(games: int) -> list:

    # set variables for monte carlo simulation
    simulation_stats = []
    wins = 0
    losses = 0

    # perform monte carlo simulation
    for i in range(games):
        # Run single game
        if single_game():
            wins = wins + 1
        else:
            losses = losses + 1

    # Calculate all stats for simulation
    simulation_stats.append(games)
    simulation_stats.append(wins)
    simulation_stats.append(losses)
    simulation_stats.append(wins/games)


    return simulation_stats


if __name__ == "__main__":
    data = main(100)
    print(data)
    print(roll())