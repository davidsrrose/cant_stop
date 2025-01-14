import random
import pandas

from itertools import combinations

class CantStopGame:
    """Class for managing the state of a cant stop game"""
    
    def __init__(self) -> None:
        self.board_progress = [0] * 11  # Columns 2 through 12 (index 0 -> 2, index 10 -> 12)
        self.progress_targets = [3, 5, 5, 9, 11, 13, 11, 9, 5, 5, 3] # Number needed to complete 
        self.goals_to_complete = []  # list of goals we are trying to complete
        self.goals_completed = []  # Track completed columns
        self.game_over = False
        self.win = False
 
    def roll(self) -> list[tuple[int, int]]:
        """Rolls 4 dice and returns all possible pairs of sums to choose from."""
        # Roll 4 dice
        roll_results = [random.randint(1, 6) for _ in range(4)]

        # Calculate all possible sums of two dice
        sums = [sum(pair) for pair in combinations(roll_results, 2)]

        # Create sum pairs as per the cant stop game rules
        sum_pairs = [
            (sums[0], sums[5]),
            (sums[1], sums[4]),
            (sums[2], sums[3])
            ]
        return sum_pairs

    def advance_board(self, sums) -> None:
        """Advance the board based on dice sums."""

        # Advance the board
        for sum in sums:
            self.board_progress[sum - 2] += 1
        
    def is_game_loss(self,chosen_sums) -> bool:
        """ Checks if game is lost """
        # Is advancing impossible
        if any(goal in chosen_sums for goal in self.goals_to_complete):
            return False
        return True

    def is_game_win(self) -> bool:
        """ Checks if game was won """
        if len(self.goals_completed) >= 3:
            self.game_over = True
            return True
        return False
    
    def is_game_over(self, sums) -> bool:
        """ Checks if game is over """
        # Game is over if win or loss
        if self.is_game_win() or self.is_game_loss(sums):
            return True
        
    def update_goals(self):
        """ Moves number from goals_to_complete to goals_completed """
        for goal in self.goals_to_complete:
            if self.board_progress[goal - 2] == self.progress_targets[goal -2]:
                self.goals_to_complete.remove(goal)
                self.goals_completed.append(goal)
                #print(f"Goal completed! {goal} has been captured")

        
if __name__ == "__main__":

    # Start game
    game = CantStopGame()

    # Check board advancing
    print(game.board_progress)
    for _ in range(9):
        game.advance_board([5])
    print(game.board_progress)

    game.goals_to_complete.append(5)
    print("goals to complete: ", game.goals_to_complete)
    print("goals completed: ", game.goals_completed)

    game.update_goals()

    print(game.board_progress)

    for _ in range(9):
        game.advance_board([2])
    print(game.board_progress)

    game.goals_to_complete.append(5)
    print("goals to complete: ", game.goals_to_complete)
    print("goals completed: ", game.goals_completed)

    game.update_goals()

    print("goals to complete: ", game.goals_to_complete)
    print("goals completed: ", game.goals_completed)
