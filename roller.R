# rolls four dice and outputs an array to the four rolls

# inputs:

# outputs:

# notes on improvements and additions to function

#-------------------------------------------------------------------------------
roller <- function() {
    # function roller outputs an array of 4 randomly generated die rolls (1-6)
    roll_vector <- sample(1:6, 4)

    # make the roll NOT RANDOM
    # roll_vector[] <-sample(c(4,7,9))

    return(roll_vector)
}