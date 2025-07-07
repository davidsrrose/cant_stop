

def choose_sum_pair(roll, goals) -> list:

    # no goals yet picked - pick the sum pair based on the sum pair that gives the best p(successful roll)

    # one goal picked

    # two goals picked

    # three goals picked - choose the sum pair with most goals advanced
    if len(goals) == 3:
        # 
        return roll[goal_advancement_rank(roll, goals)]

    return roll[0]


def goal_advancement_rank(roll, goals) -> list:
    scores = [0,0,0]

    for i in range(3):
        for sum in roll[i]:
            if sum in goals:
                scores[i] = scores[i] + 1

    index = scores.index(max(scores))
    return index