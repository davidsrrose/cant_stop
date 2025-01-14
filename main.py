from chuck_brain import choose_sum_pair 
from game import CantStopGame
from utils import time_function, spinnner_animation

def single_game() -> bool:
    """  Plays one single game of solitaire cant_stop """
    # Initialized game
    game = CantStopGame()
    is_game_over = False
    game.goals_to_complete.append(4)
    game.goals_to_complete.append(7)
    game.goals_to_complete.append(10)

    #print(" new game! ----------------------------------------------")

    while not is_game_over:

        # Roll dice
        roll = game.roll()
        #print("roll: ", roll)

        # Pick sum from roll options
        # TODO add logic for choosing sums - this is the hard part :)
        sums = choose_sum_pair(roll, game.goals_to_complete)
       #print("chosen_sums: ", sums)
        # Advance board
        game.advance_board(sums)

        # Uplodate goals 
        game.update_goals()

        # Check if game is over
        is_game_over = game.is_game_over(sums)
    
    return game.is_game_win()

@spinnner_animation
@time_function
def main(games: int) -> None:

    wins = 0
    losses = 0

    # perform monte carlo simulation
    for i in range(games):
        # Run single game
        if single_game():
            wins = wins + 1
        else:
            losses = losses + 1

    print("\n")
    print("wins: ",wins)
    print("losses: ",losses)
    print("win probability: ", wins/games)

if __name__ == "__main__":
    data = main(games = 100000)
