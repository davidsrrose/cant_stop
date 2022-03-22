# take in a sum option matrix
# return the statistically optimal sum pair for solitare cant stop
# only needed when we do not have three goals to go for yet
# zero, one, or two goals


# inputs:

# outputs:

# notes on improvements and additions to function
# assumes that the goal matrix is filled from first index and then over
# works wrong if this isnt the case!
# stupid to calculate the vector of all possible die combos every time
# re-do to just have a global vector of that info to pull
#-------------------------------------------------------------------------------
optimal_sum_picker <- function(sums = summer(roller()),
                               goals = c(0, 0, 0)) {
    # initialize variables
    # matrix to store sums and probability
    sums_and_roll_p <- cbind(sums, c(0, 0, 0))

    colnames(sums_and_roll_p) <- c(
        "sum_1",
        "sum_2",
        "roll_p"
    )

    # calculate roll probabilities for 0 goals
    if (goals[1] == 0) {
        for (i in i:3) {
            sums_and_roll_p[i, 3] <- advance_probability(sums[i, 1], sums[i, 2])
        }
    }

    # calculate roll probabilites for 1 goal
    if (goals[1] != 0 && goals[2] == 0) {
        for (i in i:3) {
            sums_and_roll_p[i, 3] <- advance_probability(sums[i, 1], sums[i, 2], goals[1])
        }
    }

    # calculate roll probabilites for 2 goals
    if (goals[2] != 0) {
        for (i in i:3) {
            sums_and_roll_p[i, 3] <- advance_probability(sums[i, 1], sums[i, 2])
        }
    }

    return(sums_and_roll_p)
}