# chooses the sum pair to pick, given:
# inputs:
# sums - sums that were just rolled
# board - the current state of the game board
# goals - the goald

# outputs:
# the sums we want to choose - by column of the input sums matrix

# notes on improvements and additions to function

#-------------------------------------------------------------------------------
# Picks based on "Chuck Logic"
chuck_logic <- function(sums,
                        game_board_df,
                        sum_score_df,
                        goals) {

  # initialize variables
  # column of the sum matrix that we want to pick
  returncol <- as.integer(0)



  # "chuck logic" flow for choosing which pair to go with
  # if only one sum satisfies the max number of goals, choose that pair
  # if (max(scorematrix[13, ]) == 3) {
  # return the column which as the 3
  # (which(max max(scorematrix[13,])==3)
  #   returncol <- (which.max(scorematrix[13, ]))
  # }
  # if there is a tie for max goals, choose on gap, then on gap p
  # if (max(scorematrix[13, ]) == 2.5) {
  # choose based on gap - one highest gap
  #  if (max(scorematrix[14, ]) == 3) {
  #    returncol <- (which.max(scorematrix[14, ]))
  #  }
  # choose based on gap - tie for highest gap
  # if (max(scorematrix[14, ]) == 2.5) {
  # choose based on gap(p) - one lowest gap(p)
  #  if (max(scorematrix[15, ]) == 1) {
  # returncol <- (which.min(scorematrix[15, ]))
  # }
  # choose based on gap(p) - tie for lowest gap(p)
  # randomly select one of the columns tied for lowest gap(p)
  # if (max(scorematrix[15, ]) == 1.5) {
  #  returncol <- (which.min(scorematrix[15, ]))
  # }
  # }
  # }
  # nothing was picked so pick randomly
  # if (returncol == 0) {
  #   returncol <- sample(1:3, 1)
  # }
  return(sums[, returncol])
} #####################################################################################################