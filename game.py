import random
from itertools import combinations

class CantStopGame:
    """Class for managing the state of a single game"""
    
    def __init__(self) -> None:
        self.board_progress = [0] * 11  # Columns 2 through 12 (index 0 -> 2, index 10 -> 12)
        self.number_targets = [3, 5, 7, 9, 11, 13, 11, 9, 7, 5, 3] # Number needed to complete 
        self.goals = [3]  # Goal of 3 completed columns
        self.completed_columns = []  # Track completed columns
        self.game_over = False
        self.win = False

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

    def advance_board(self, chosen_sums) -> None:
        """Advance the board based on dice sums."""
        for sum in chosen_sums:
            self.board_progress[sum - 2] += 1

    def is_game_loss(self,chosen_sums) -> bool:
        """ Checks current game for terminal status. """
        # is advancing impossible
        if any(goal in chosen_sums for goal in self.goals):
            return False
        return True

    def is_game_win(self) -> bool:
        """ Checks if game was won """
        if len(self.completed_columns) >= 3:
            self.game_over = True
            return True
        return False


# Example usage
game = CantStopGame()
print(game.board_progress)
game.advance_board([2,8])
print(game.board_progress)
game.advance_board([7])
print(game.board_progress)
