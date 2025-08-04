from game_client import CantStopGame

from loguru import logger

def single_game() -> bool:
    """  Plays one single game of solitaire cant_stop """
    # Initialize game
    game = CantStopGame()

    # Preset goals (dev!)
    game.goals.append(4)
    game.goals.append(7)
    game.goals.append(10)

    sums = None

    # Run solitaire game of cant stop
    while not game.is_game_over(sums):

        # Roll dice
        roll = game.roll()
        
        # Pick sum from roll options
        sums = game.choose_sum_pair(roll)

        # Advance board
        game.advance_board(sums)

        # Update goals 
        game.update_goals()

        # Log game progress
        game.log_board_progress()

    return game.is_game_win()


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
    data = main(games = 10)
