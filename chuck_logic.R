# chooses the sum pair to pick, given:
# inputs:
# sums - sums that were just rolled
# board - the current state of the game board
# goals - the goald

# outputs:
# the sums we want to choose - by column of the input sums matrix

# notes on improvements and additions to function
# does this need to take in goals?

#-------------------------------------------------------------------------------
# Picks based on "Chuck Logic"
chuck_logic <- function(sums,
                        game_board_df,
                        sum_score_df,
                        goals) {

  # initialize variables
  # column of the sum matrix that we want to pick
  chosen_sum_row <- as.integer(0)

  # advancement probabilities of roll

  print("chuck logic")
  print(sums)
  print(goals)
  print(sum_score_df)
  print(game_board_df)


  # "chuck logic" flow for choosing which pair to go with

  # if we have zero goals so far
  if (goals[1] == 0) {

  }
  # if we have one goal established
  if (goals[1] != 0 && goals[2] == 0) {


  }
  # if we have two goals establihsed
  if (goals[2] != 0) {
  }

  # just select first sum for now########################################
  chosen_sum_row <- 1

  print(sums[chosen_sum_row, ])
  return(sums[chosen_sum_row, ])
} #####################################################################################################