import argparse
import numpy as np
import matplotlib.pyplot as plt
from levels.level import Level
from levels.env_config import *


def parse():
    parser = argparse.ArgumentParser(description="Tabular Q-Learning")
    parser.add_argument("--num_episodes", default=1000, type=int)
    parser.add_argument("--level", default=1, type=int)
    parser.add_argument("--gamma", default=1, type=float)
    parser.add_argument("--alpha", default=0.1, type=float)
    parser.add_argument("--vis", action="store_true")
    parser.set_defaults(vis=False)
    args = parser.parse_args()
    return args


def eps_greedy_action_select(Q, s, eps=0.01):
    """
    Chooses an action following the epsilon greedy policy.
    Inputs:
        - Q: the state-action value function to select from
        - s: the current of the agent
        - eps: how often to choose a random action uniformly
    Outputs:

    """
    if np.random.uniform() < eps:
        return -1, np.random.randint(0, 4)
    else:
        max_Q = np.float64("-inf")
        a = 0
        for i in range(0, 5):
            if s not in Q[i]:
                Q[i][s] = 0  # instantiate this state, action pair if it does not exist
            Q_i = Q[i][s]
            if Q_i > max_Q:
                max_Q = Q_i
                a = i
        return max_Q, a
    

def validate(Q):
    s, done = env.reset(), False
    r_total = 0
    step = 1
    while not done and step < 200:
        _, a = eps_greedy_action_select(Q, s, 0)
        s, r, done = env.step(a)
        r_total += r
        step += 1


if __name__ == "__main__":
    args = parse()

    print("Args: ", args)

    if args.level == 1:
        env = Level(start_pos=(3, 6), base_env=level_one_env)

    elif args.level == 2:
        env = Level(
            start_pos=(6, 3),
            base_env=level_two_env,
            soft_switches=level_two_soft_switches,
            hard_switches=level_two_hard_switches,
        )

    elif args.level == 3:
        env = Level(start_pos=(4, 3), base_env=level_three_env)

    elif args.level == 4:
        env = Level(start_pos=(6, 4), base_env=level_four_env)

    elif args.level == 5:
        env = Level(
            start_pos=(2, 15),
            base_env=level_five_env,
            soft_switches=level_five_soft_switches,
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
            hard_switches=level_seven_hard_switches
        )

    elif args.level == 8:
        env = Level(
            start_pos=(6, 4),
            base_env=level_eight_env,
            teleport_switches=level_eight_teleport_switches
        )
    elif args.level == 9:
        env = Level(
            start_pos=(4, 4),
            base_env=level_nine_env,
            teleport_switches=level_nine_teleport_switches
        )

    # 0 -> Right
    # 1 -> Up
    # 2 -> Left
    # 3 -> Down
    # 5 -> Switch Focus
    Q = [{}, {}, {}, {}, {}]

    act_to_lang = {0: "Right", 1: "Up", 2: "Left", 3: "Down", 4: "Switch Focus"}

    for e in range(args.num_episodes):
        s, done = env.reset(), False

        steps = 0
        r_total = 0
        while not done:
            _, a = eps_greedy_action_select(Q, s)
            s_prime, r, done = env.step(a)
            Q_prime, _ = eps_greedy_action_select(Q, s_prime, eps=0)
            Q[a][s] = Q[a][s] + args.alpha * (r + args.gamma * Q_prime - Q[a][s])
            s = s_prime
            
            r_total += r
            # print(f'Action: {a} | Focus: {env.get_block().get_focus()} | Reward: {r_total}')
            # print(env.get_state())
            # if steps % 200 == 0:
            #     input("Press enter to continue...")
            steps += 1

        print(f'Finished ep {e}, total return: {r_total}')

    # Final Route
    print("----- Final Route ----- ")
    s, done = env.reset(), False
    r_total = 0
    step = 1
    while not done and step < 200:
        _, a = eps_greedy_action_select(Q, s,0)
        s, r, done = env.step(a)
        print(f"Action: {act_to_lang[a]} | Done: {done} | Reward: {r_total}")
        r_total+=1
        step += 1
