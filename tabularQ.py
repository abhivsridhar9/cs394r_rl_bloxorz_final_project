import argparse
import numpy as np
from levels.level import Level
from levels.env_config import *


def parse():
    parser = argparse.ArgumentParser(description="Tabular Q-Learning")
    parser.add_argument("--num_episodes", default=1000)
    parser.add_argument("--level", default=1, type=int)
    parser.add_argument("--gamma", default=1)
    parser.add_argument("--alpha", default=0.1)
    args = parser.parse_args()
    return args


def eps_greedy_action_select(Q, s, eps=1e-2):
    """
    Chooses an action following the epsilon greedy policy.
    Inputs:
        - Q: the state-action value function to select from
        - s: the current of the agent
        - eps: how often to choose a random action uniformly
    Outputs:

    """
    if np.random.uniform() < eps:
        return -1, np.random.randint(0, 3)
    else:
        max_Q = np.float64("-inf")
        a = 0
        for i in range(0, 4):
            if s not in Q[i]:
                Q[i][s] = 0  # instantiate this state, action pair if it does not exist
            Q_i = Q[i][s]
            if Q_i > max_Q:
                max_Q = Q_i
                a = i
        return max_Q, a


if __name__ == "__main__":
    args = parse()

    print("Args: ", args)

    if args.level == 1:
        env = Level(start_pos=(3, 6), base_env=level_one_env)

    elif args.level == 2:
        env = Level(
            start_pos=(6, 3),
            base_env=level_two_env,
            circle_switches=level_two_circle_switches,
            x_switches=level_two_x_switches,
        )

    elif args.level == 3:
        env = Level(start_pos=(4, 3), base_env=level_three_env)

    elif args.level == 4:
        env = Level(start_pos=(6, 4), base_env=level_four_env)

    elif args.level == 5:
        env = Level(
            start_pos=(2, 15),
            base_env=level_five_env,
            circle_switches=level_five_circle_switches,
        )
    elif args.level == 6:
        env = Level(
            start_pos=(4, 3),
            base_env=level_six_env,
        )

    elif args.level == 7:
        env = Level(
            start_pos=(4, 4),
            base_env=level_seven_env,
            x_switches=level_seven_x_switches
        )

    # 0 -> Right
    # 1 -> Up
    # 2 -> Left
    # 3 -> Down
    Q = [{}, {}, {}, {}]

    for e in range(args.num_episodes):
        s, done = env.reset(), False

        while not done:
            _, a = eps_greedy_action_select(Q, s)
            s_prime, r, done = env.step(a)
            Q_prime, _ = eps_greedy_action_select(Q, s_prime, eps=0)
            Q[a][s] = Q[a][s] + args.alpha * (r + args.gamma * Q_prime - Q[a][s])
            s = s_prime

            # print("Action: ",a)

    # Final Route
    act_to_lang = {0: "Right", 1: "Up", 2: "Left", 3: "Down"}
    print("----- Final Route ----- ")
    s, done = env.reset(), False

    r_total = 0
    step = 1
    while not done:
        _, a = eps_greedy_action_select(Q, s, 0)
        r_total += r
        s, r, done = env.step(a)
        print(f"Action: {act_to_lang[a]} | Done: {done} | Reward: {r_total}")
        step += 1
