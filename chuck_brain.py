def choose_sum_pair(roll) -> list:
    for sum_pair in roll:
        for sum in sum_pair:
            if sum == 7:
                return sum_pair          

    return roll[0]
