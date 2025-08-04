import random

from chuck_brain import choose_sum_pair
from itertools import combinations
from loguru import logger


class CantStopGame:
    """Class for managing the state of a cant stop game"""

    def __init__(self) -> None:
        self.board_labels = [
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
        ]  # Number needed to complete each sum
        self.board_progress = (
            [0] * 11
        )  # Columns for dice sums 2 through 12 (index 0 for sum 2, index 10 for sum 12)
        self.progress_targets = [
            3,
            5,
            5,
            9,
            11,
            13,
            11,
            9,
            5,
            5,
            3,
        ]  # Number needed to complete each sum
        self.progress_targets = [
            3,
            5,
            5,
            9,
            11,
            13,
            11,
            9,
            5,
            5,
            3,
        ]  # Number needed to complete each sum
        self.goals = []  # List of goals for the game
        self.goals_not_completed = []  # List of goals we still need to complete
        self.goals_completed = []  # List completed goals
        self.win = False

    def roll(self) -> list[tuple[int, int]]:
        """Rolls 4 dice and returns all possible pairs of sums to choose from."""
        # Roll 4 dice
        roll_results = [random.randint(1, 6) for _ in range(4)]

        # Calculate all possible sums of two dice
        sums = [sum(pair) for pair in combinations(roll_results, 2)]

        # Create sum pairs as per the cant stop game rules
        sum_pairs = [(sums[0], sums[5]), (sums[1], sums[4]), (sums[2], sums[3])]
        logger.info(f"Dice rolled - {roll_results}, sum pairs {sum_pairs}")
        return sum_pairs

    def advance_board(self, sums) -> None:
        """Advance the board based on dice sums."""

        # Advance the board
        for sum in sums:
            self.board_progress[sum - 2] += 1

    def is_game_loss(self, chosen_sums) -> bool:
        """Checks if game is lost"""
        # Is advancing impossible
        if any(goal in chosen_sums for goal in self.goals_to_complete):
            return False
        logger.warning("Game lost")
        return True

    def is_game_win(self) -> bool:
        """Checks if game was won"""
        if len(self.goals_completed) >= 3:
            self.game_over = True
            logger.success("Game won!")
            return True
        return False

    def is_game_over(self, sums: list | None) -> bool:
        """Checks if game is over"""
        # No sums means no roll yet, so game not over
        if sums is None:
            return False

        # Game is over if win or loss
        if self.is_game_win() or self.is_game_loss(sums):
            return True

        return False

    def update_goals(self) -> None:
        """Update goals_to_complete, goals_completed"""
        for goal in self.goals:
            if self.board_progress[goal - 2] == self.progress_targets[goal - 2]:
                self.goals_to_complete.remove(goal)
                self.goals_completed.append(goal)
                logger.warning(f"Goal of {goal} captured!")
                logger.info(f"Goals updated to {self.goals_to_complete}")

    def process_game_state(self, roll) -> list[int, int]:
        """given game state, determines rolls to pick, or goals (as needed)"""
        chosen_sum_pair = choose_sum_pair(
            roll, self.goals_to_complete, self.goals_completed
        )
        logger.info(f"Chose sum pair {chosen_sum_pair}")
        return chosen_sum_pair

    def log_board_progress(self) -> None:
        logger.info(f"                {self.board_labels}")
        logger.info(f"Board progress: {self.board_progress}")


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
