# runs one cant stop game, given inputs
# not set up for good decision making.
# only picks ##s then rolls until loss. never stops

# inputs:
# brain function to use

# outputs:
# game board at the end of the game

# notes on improvements and additions to function
# get the p(winning on first roll)
# get the p(winning on the first roll, with dad's #s)
# get the p(winning on the first roll)
# difficulty of first roll win probability
# is that influened by the "brain" for the game aka decision making engine
# update to class? method for calling the "chuck_brain" as a part of a class
# of decision making functions

#-------------------------------------------------------------------------------
single_game_run <- function() {

    # initialize variables
    # dataframe which represents the board during play
    game_board_df <- data.frame(
        matrix(
            0,
            nrow = 11,
            ncol = 2
        )
    )
    # name & fill rows & columns
    colnames(game_board_df) <- c(
        "current_progress",
        "rolls_required_to_capture"
    )
    rownames(game_board_df) <- c(2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
    game_board_df$rolls_required_to_capture <-
        c(3, 5, 7, 9, 11, 13, 11, 9, 7, 5, 3)
    game_board_df$current_progress <- rep(0, 11)

    # matrix of potential sums to choose after rolling dice
    sums <- matrix(0, nrow = 3, ncol = 2)

    # sums chosen for turn
    sums_chosen <- c(0, 0)

    # goal numbers for our game
    goals <- c(0, 0, 0)

    # dataframe of metrics about potential roll
    sum_score_df <- data.frame(matrix(0, nrow = 3, ncol = 10))

    # exit variable for each game simulated
    game_over <- as.logical(FALSE)


    # simulate an attempt at a "perfect game"
    while (game_over == FALSE) {

        # roll dice and get potential sums
        sums <- summer(roller())

        # calculate metrics for the sums
        sum_score_df <- sum_score_df_generator(
            sums,
            game_board_df,
            goals
        )
        print("here")
        print(sum_score_df)
        print(sums)
        # choose which sum pair to pick







        # advance the board (only if its on a goal though, only if it hasnt been captured)
        for (j in 1:2) {
            # if the sum chosen is one of our goals & the sum chosen is not already captured

            # if we do not advance any numbers up the board, then we bust

            # check if board to see if we won, busted
            # win - check all goals, if we got all 3, we win
            for (j in 1:11) {
                if (board[1, j] == board[2, j]) {
                    captured <- captured + 1
                }
            }
            if (captured == 3) {
                wins <- wins + 1
                done <- TRUE
            }
            # count games to throw out - the game did not organically start with a chuck combo (4,7,9)
            # print("WHILE LOOP (roll the dice)")
            # print(sums)
            # I dont know
            # random
            # hightest probability of being rolled again?
            # go for numbers
            # print(board)
        }



        # remove this once check function is working properly
        game_over <- TRUE
    }
    return(game_board_df)
}