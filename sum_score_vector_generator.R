# take in current game state and
# return vector of metrics for the sum give sum pair

# inputs:

# outputs:

# notes on improvements and additions to function
# this seems extremely bad and confusing - got to be a better way??

#-------------------------------------------------------------------------------
sum_score_vector_generator <- function(sum_pair,
                                       game_board_df,
                                       goals) {
    # initalize variables
    # vector of metrics about sum pairs, for deciding which sum to use
    sum_score_vector <- rep(0, 10)

    # calculate metrics
    # 1 goal 1 advancement
    # 2 goal 2 advancement
    # 3 goal 3 advancement
    for (i in 1:3) {
        # sum 1
        if (goals[i] == sum_pair[1]) {
            sum_score_vector[1] <- sum_score_vector[1] + 1
        }
        # sum 2
        if (goals[i] == sum_pair[2]) {
            sum_score_vector[1] <- sum_score_vector[1] + 1
        }
    }

    # 4 total goal advancement
    sum_score_vector[4] <- sum(sum_score_vector[1:3])

    # 5 goal 1 rolls to complete
    # 6 goal 2 rolls to complete
    # 7 goal 3 rolls to complete
    for (i in 1:3) {
        # only if goal is non-zero
        if (goals[i] != 0) {
            sum_score_vector[i + 4] <-
                game_board_df$rolls_needed_to_capture[goals[i] - 1] -
                game_board_df$current_progress[goals[i] - 1]
        }
    }

    # 8 goal 1 percent completed
    # 9 goal 2 percent completed
    # 10 goal 3 percent completed

    for (i in 1:3) {
        # only if goal is non-zero
        if (goals[i] != 0) {
            sum_score_vector[i + 7] <-
                game_board_df$current_progress[goals[i] - 1] /
                    game_board_df$rolls_needed_to_capture[goals[i] - 1]
        }
    }
    return(sum_score_vector)
}