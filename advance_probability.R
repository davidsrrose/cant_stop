# take in either two or three dice sums
# and returns the probability of rolling those combos


# inputs:

# outputs:

# notes on improvements and additions to function
# probabily stupid make this for loop every single time
# re-do to just have a global vector of that info to pull from?
#-------------------------------------------------------------------------------
advance_probability <- function(goal_1, goal_2 = 0, goal_3 = 0) {
    # initialize variables
    # count of times sums are rolled
    count <- 0
    # probabilty of advancing, given goal number
    probability <- 0

    # sums of the die rolls in the nested for loop of n00bery
    sums <- matrix(0, nrow = 3, ncol = 2)

    # roll all combos and count times at the goal is in a sum
    # this is probably really wrong
    for (i in 1:6) {
        for (j in 1:6) {
            for (k in 1:6) {
                for (m in 1:6) {
                    sums <- summer(c(i, j, k, m))
                    # add to count if any of our goals are in the sums matrix
                    if (goal_1 %in% sums ||
                        goal_2 %in% sums ||
                        goal_3 %in% sums) {
                        count <- count + 1
                    }
                }
            }
        }
    }

    # calculate probability
    probability <- count / (6^4)

    return(probability)
}