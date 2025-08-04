from loguru import logger

def choose_sum_pair(roll, goals_to_complete, goals_completed) -> list:

    # no goals yet picked - pick the sum pair based on the sum pair that gives the best p(successful roll)
    if len(goals_to_complete) == 0:
        pass

    # one goal picked

    # two goals

    # three goals - choose the sum pair with most goals advanced

    return roll[goal_advancement_rank(roll, goals)]

def goal_advancement_rank(roll, goals) -> list:
    sum_scores = [0,0,0]

    for i in range(3):
        for sum in roll[i]:
            if sum in goals:
                sum_scores[i] = sum_scores[i] + 1
    logger.info(f'Sum scores: {sum_scores}')
    index = sum_scores.index(max(sum_scores))
    return index

if __name__ == "__main__":
    sum_pairs = [(4, 12), (7, 9), (7, 9)]
    goals = [4,7,10]
    goal_advancement_rank(sum_pairs, goals)
