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
    parser.add_argument("--mode", default="s", type=str)
    parser.add_argument("--num_trials", default=1, type=int)
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

    return r_total
        

def get_env(level):
    if level == 1:
        env = Level(start_pos=(3, 6), base_env=level_one_env)

    elif level == 2:
        env = Level(
            start_pos=(6, 3),
            base_env=level_two_env,
            soft_switches=level_two_soft_switches,
            hard_switches=level_two_hard_switches,
        )

    elif level == 3:
        env = Level(start_pos=(4, 3), base_env=level_three_env)

    elif level == 4:
        env = Level(start_pos=(6, 4), base_env=level_four_env)

    elif level == 5:
        env = Level(
            start_pos=(2, 15),
            base_env=level_five_env,
            soft_switches=level_five_soft_switches,
        )
    elif level == 6:
        env = Level(
            start_pos=(4, 3),
            base_env=level_six_env,
        )

    elif level == 7:
        env = Level(
            start_pos=(4, 4),
            base_env=level_seven_env,
            hard_switches=level_seven_hard_switches,
        )

    elif level == 8:
        env = Level(
            start_pos=(6, 4),
            base_env=level_eight_env,
            teleport_switches=level_eight_teleport_switches,
        )
    elif level == 9:
        env = Level(
            start_pos=(4, 4),
            base_env=level_nine_env,
            teleport_switches=level_nine_teleport_switches
        )

    elif args.level == 10:
        env = Level(
            start_pos=(2, 12),
            base_env=level_ten_env,
            soft_switches=level_ten_soft_switches,
            hard_switches=level_ten_hard_switches,
            teleport_switches=level_ten_teleport_switches,
        )

    return env

def Q_learning(env, num_episodes, alpha, gamma, num_trials):
    # 0 -> Right
    # 1 -> Up
    # 2 -> Left
    # 3 -> Down
    # 5 -> Switch Focus
    Q = [{}, {}, {}, {}, {}]

    act_to_lang = {0: "Right", 1: "Up", 2: "Left", 3: "Down", 4: "Switch Focus"}
    
    r_count_trial = np.zeros(num_episodes, dtype=np.float64)
    
    for t in range(num_trials):
        r_list = []
        for e in range(num_episodes):
            s, done = env.reset(), False
            r_ep = 0
            while not done:
                _, a = eps_greedy_action_select(Q, s)
                s_prime, r, done = env.step(a)
                Q_prime, _ = eps_greedy_action_select(Q, s_prime, eps=0)
                Q[a][s] = Q[a][s] + alpha * (r + gamma * Q_prime - Q[a][s])
                s = s_prime
                r_ep += r
            r_list.append(r_ep)
            print(f"Episode {e} done | Reward = {r_ep}")
        r_count_trial += np.clip(np.array(r_list), -200, 0)

    # Final Route
    print("----- Final Route ----- ")
    s, done = env.reset(), False
    r_total = 0
    step = 1
    while not done and step < 200:
        _, a = eps_greedy_action_select(Q, s, 0)
        s, r, done = env.step(a)
        print(f"Action: {act_to_lang[a]} | Done: {done} | Reward: {r_total}")
        r_total += 1
        step += 1
        
    return r_count_trial / num_trials


if __name__ == "__main__":
    args = parse()

    print("Args: ", args)
    
    if args.mode == "s":
        env = get_env(args.level)
        r_list = Q_learning(env, args.num_episodes, args.alpha, args.gamma, args.num_trials)
        plt.plot(range(args.num_episodes), r_list, label=f"Level {args.level}")
    elif args.mode == "as":
        for level in range(1,5):
            env = get_env(level)
            r_list = Q_learning(env, args.num_episodes, args.alpha, args.gamma, args.num_trials)
            plt.plot(range(args.num_episodes), r_list, label=f"Level {level}")
    elif args.mode == "o":
        pass
    
    plt.title("Returns Across Episodes")
    plt.legend()
    plt.grid()
    plt.xlabel("Episode")
    plt.ylabel("Return")
    plt.show()
