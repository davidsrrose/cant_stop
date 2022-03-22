# take in current game state and return dataframe of metrics on

# inputs:

# outputs:

# notes on improvements and additions to function
# this seems extrememly clunky and confusing - got to be a better way

#-------------------------------------------------------------------------------
sum_score_df_generator <- function(sums,
                                   game_board_df,
                                   goals) {

    # initalize variables
    # vector of metrics about sum pairs, for deciding which sum to use
    sum_score_df <- data.frame(matrix(0, nrow = 3, ncol = 13))
    # label sum score dataframe
    rownames(sum_score_df) <- c(
        "sum_pair_1",
        "sum_pair_2",
        "sum_pair_3"
    )
    colnames(sum_score_df) <- c(
        "goal_1_advance",
        "goal_2_advance",
        "goal_3_advance",
        "total_goal_advance",
        "goal_1_rolls_to_complete",
        "goal_2_rolls_to_complete",
        "goal_3_rolls_to_complete",
        "goal_1_percent_complete",
        "goal_2_percent_complete",
        "goal_3_percent_complete",
        "goal_1_advance_probability",
        "goal_2_advance_probability",
        "goal_3_advance_probability"
    )


    for (i in 1:3) {
        sum_score_df[i, ] <- sum_score_vector_generator(
            sums[i, ],
            game_board_df,
            goals
        )
    }
    return(sum_score_df)
}