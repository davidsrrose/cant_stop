# checks given game board, sums, and goals to determine if game is over - "bust"

# inputs:

# outputs:

# notes on improvements and additions to function

#-------------------------------------------------------------------------------
is_game_over <- function(game_board_df, sums_chosen, goals) {

    # initialize variables
    game_over <- FALSE
    print("is game over function")
    print(sums_chosen)
    print(goals)


    # we cannot advance (no goals match)
    if (!(any(sums_chosen %in% goals))) {
        game_over <- TRUE
        print("game over chosen sums dont match goals")
    }

    # we have captured all 3 numbers
    if (sum(game_board_df$current_progress ==
        game_board_df$rolls_required_to_capture)) {
        game_over <- TRUE
        print("game over CUZ WIN!")
    }

    return(game_over)
}