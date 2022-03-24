# updates game board based on sums chosen

# inputs:

# outputs:

# notes on improvements and additions to function

#-------------------------------------------------------------------------------
advance_game_board <- function(sums_chosen,
                               game_board_df,
                               goals) {
    for (i in 1:2) {
        # only advance for the chosen sum if it is not captured!,
        # and only advance if the sum chosen is a goal
        if ((game_board_df$current_progress[sums_chosen[i] - 1] !=
            game_board_df$rolls_required_to_capture) &&
            (sums_chosen[i] %in% goals){
                
            game_board_df$current_progress[sums_chosen[i] - 1] <-
                game_board_df$current_progress[sums_chosen[i] - 1] + 1
        }
    }
    return(game_board_df)
}