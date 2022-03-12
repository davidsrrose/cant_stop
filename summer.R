# take in a roll of 4 dice and returns the 3 sum options

# inputs:

# outputs:

# notes on improvements and additions to function

#-------------------------------------------------------------------------------
summer <- function(roll_vector) {
    # initialize variables
    sum_matrix <- matrix(0, nrow = 3, ncol = 2)

    # fill sum_array
    # sum pair 1
    sum_matrix[1, 1] <- roll_vector[1] + roll_vector[2]
    sum_matrix[1, 2] <- roll_vector[3] + roll_vector[4]
    # sum pair 2
    sum_matrix[2, 1] <- roll_vector[1] + roll_vector[3]
    sum_matrix[2, 2] <- roll_vector[2] + roll_vector[4]
    # sum pair 3
    sum_matrix[3, 1] <- roll_vector[1] + roll_vector[4]
    sum_matrix[3, 2] <- roll_vector[2] + roll_vector[3]

    # label sum_matrix
    rownames(sum_matrix) <- c(
        "pair_1",
        "pair_2",
        "pair_3"
    )
    colnames(sum_matrix) <- c(
        "sum_1",
        "sum_2"
    )

    return(sum_matrix)
}