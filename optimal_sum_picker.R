# take in a sum option matrix
# return the statistically optimal sum pair for solitare cant stop
# only needed when we do not have three goals to go for yet
# zero, one, or two goals


# inputs:

# outputs:

# notes on improvements and additions to function
# stupid to calculate the vector of all possible die combos every time
# re-do to just have a global vector of that info to pull
#-------------------------------------------------------------------------------
optimal_sum_picker <- function(sums = summer(roller()),
                               goals = c(0, 0, 0)) {
    # initialize variables
    # matrix to store sums and probability
    sums_and_roll_p <- cbind(sums, c(0, 0, 0))

    colnames(sums_and_roll_p) <- c("sum_1", "sum_2", "roll_p")
    # rownames(sums_and_roll_p) <- c("pair_1", "pair_2", "pair_3")
    print(sums)

    # calculate roll probability for 0 goals
    if (goals[1] & goals[2] & goals[3] == 0) {
        for (i in i:3) {
            print("for loopss")
            print(sums[i, 1])
            print(sums[i, 2])
            sums_and_roll_p[i, 3] <- advance_probability(sums[i, 1], sums[i, 2])
        }
    }

    return(sums_and_roll_p)
}