import argparse
import numpy as np
from Levels.levelone import LevelOne

ALPHA = 0.1
GAMMA = 1

def parse():
    parser = argparse.ArgumentParser(description='Tabular Q-Learning')
    parser.add_argument('--num_episodes', default=1000)
    parser.add_argument("--level", default=1, type=int)
    args = parser.parse_args()
    return args

def eps_greedy_action_select(Q, s, eps=1e-4):
    if np.random.uniform() < eps:
        return np.random.randint(0, 3)
    else:
        max_Q = np.float64("-inf")
        max_Q_i = 0
        for i in range(0, 4):
            if s not in Q[i]:
                Q[i][s] = 0     # instantiate this state, action pair if it does not exist
            Q_i = Q[i][s]
            if Q_i > max_Q:
                max_Q = Q_i
                max_Q_i = i
        return max_Q_i
    
def greedy_Q(Q, s):
    max_Q = np.float64("-inf")
    for i in range(0, 4):
        if s not in Q[i]:
            Q[i][s] = 0        # instantiate this state, action pair if it does not exist
        Q_i = Q[i][s]
        if Q_i > max_Q:
            max_Q = Q_i
    return max_Q


if __name__ == '__main__':
    args = parse()

    if args.level == 1:
        env = LevelOne()

    # 0 -> Right
    # 1 -> Up
    # 2 -> Left
    # 3 -> Down
    Q = [{}, {}, {}, {}]

    for _ in range(args.num_episodes):
        s, done = env.reset(), False

        while not done:
            a = eps_greedy_action_select(Q, s)
            s_prime, r, done = env.step(a)
            max_Q_s_prime_a = greedy_Q(Q, s_prime)
            Q[a][s] = Q[a][s] + ALPHA * (r + GAMMA * max_Q_s_prime_a - Q[a][s])
            s = s_prime

    # Final Route
    act_to_lang = {
        0: 'Right',
        1: 'Up',
        2: 'Left',
        3: 'Down'
    }
    print('----- Final Route ----- ')
    s, done = env.reset(), False

    r_total = 0
    while not done:
        a = eps_greedy_action_select(Q, s, 0)
        s, r, done = env.step(a)
        r_total += r
        print(f'Action: {act_to_lang[a]} | Done: {done} | Reward: {r_total}')
