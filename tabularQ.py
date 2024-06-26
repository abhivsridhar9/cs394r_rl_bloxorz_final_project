import argparse
import numpy as np
from pickle import dumps
from sys import getsizeof
from levels.level import Level
from levels.env_config import *


def parse():
    parser = argparse.ArgumentParser(description="Tabular Q-Learning")
    parser.add_argument("--num_episodes", default=2000, type=int)
    parser.add_argument("--level", default=1, type=int)
    parser.add_argument("--gamma", default=1, type=float)
    parser.add_argument("--alpha", default=0.1, type=float)
    parser.add_argument("--mode", default="single_level", type=str)
    parser.add_argument("--num_trials", default=25, type=int)
    parser.add_argument("--output_dir", default="./results", type=str)
    args = parser.parse_args()
    return args


def eps_greedy_action_select(Q, s, eps=0.1):
    """
    Chooses an action following the epsilon greedy policy.
    Inputs:
        - Q: the state-action value function to select from
        - s: the current of the agent
        - eps: how often to choose a random action uniformly
    Outputs:

    """
    if np.random.uniform() < eps:
        a = np.random.randint(0, 4)
        if s not in Q[a]:   # instantiate this state, action pair if it does not exist
            Q[a][s] = 0
        return -1, a
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

        
def validate(Q, env):
    s, done = env.reset(), False
    r_total = 0
    step = 1
    while not done and step < 200:
        _, a = eps_greedy_action_select(Q, s, 0) # make the greedy selection
        s, r, done = env.step(a)
        r_total += r
        step += 1
    return r_total

def validate_playthrough(Q):
    level = 1
    env, _ = get_env(level)
    s, done_lvl_ten, done = env.reset(), False, False
    r_total = 0
    step = 1

    while not done_lvl_ten and step < 300:
        _, a = eps_greedy_action_select(Q, s, 0)
        s, r, done = env.step(a)
        step += 1
        r_total += r
        if done and (level != 10):
            # transition to the next level if the agent finished the current level and the current level was not level ten
            level += 1
            env, _ = get_env(level)
            s, done_lvl_ten, done = env.reset(), False, False
        elif done and (level == 10):
            # signal that we are completely finished if the agent finished the current level and the agent is on level ten
            done_lvl_ten = True
    return r_total


def get_env(level):
    if level == 1:
        env = Level(start_pos=(3, 6), base_env=level_one_env)
        optimal_return = -6

    elif level == 2:
        env = Level(
            start_pos=(6, 3),
            base_env=level_two_env,
            soft_switches=level_two_soft_switches,
            hard_switches=level_two_hard_switches,
        )
        optimal_return = -16

    elif level == 3:
        env = Level(start_pos=(4, 3), base_env=level_three_env)
        optimal_return = -18

    elif level == 4:
        env = Level(start_pos=(6, 4), base_env=level_four_env)
        optimal_return = -27

    elif level == 5:
        env = Level(
            start_pos=(2, 15),
            base_env=level_five_env,
            soft_switches=level_five_soft_switches,
        )
        optimal_return = -32

    elif level == 6:
        env = Level(
            start_pos=(4, 3),
            base_env=level_six_env,
        )
        optimal_return = -34

    elif level == 7:
        env = Level(
            start_pos=(4, 4),
            base_env=level_seven_env,
            hard_switches=level_seven_hard_switches,
        )
        optimal_return = -43

    elif level == 8:
        env = Level(
            start_pos=(6, 4),
            base_env=level_eight_env,
            teleport_switches=level_eight_teleport_switches,
        )
        optimal_return = -10

    elif level == 9:
        env = Level(
            start_pos=(4, 4),
            base_env=level_nine_env,
            teleport_switches=level_nine_teleport_switches
        )
        optimal_return = -28

    elif level == 10:
        env = Level(
            start_pos=(2, 12),
            base_env=level_ten_env,
            soft_switches=level_ten_soft_switches,
            hard_switches=level_ten_hard_switches,
            teleport_switches=level_ten_teleport_switches,
        )
        optimal_return = -61

    return env, optimal_return


def Q_learning(env, num_episodes, alpha, gamma, num_trials, optimal_return, output_path):
    # 0 -> Right
    # 1 -> Up
    # 2 -> Left
    # 3 -> Down
    # 5 -> Switch Focus
    
    # Metric trackers
    r_count_trial = np.zeros(num_episodes, dtype=np.float64)
    step_count_trial = 0
    dict_size_trial = 0
    
    for t in range(num_trials):
        print(f'Starting trial {t}...')
        Q = [{}, {}, {}, {}, {}]
        early_stop_buffer = np.ones(10, dtype=np.float64) * -1000
        converged = False
        step_count = 0
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
                step_count += 1
            # update the metric trackers with the results of the episode
            r_count_trial[e] += r_ep
            early_stop_buffer[e % 10] = validate(Q, env)
            if (not converged) and (np.mean(early_stop_buffer) == optimal_return):
                converged = True
                print('Agent has converged to the optimal solution for this level...')
                dict_size_trial += getsizeof(dumps(Q)) # pickle the dict and check the size
                step_count_trial += step_count
        
        # if the agent did not reach early stopping save the stats still
        if not converged:
            print('Agent did not meet the standards for convergence...')
            dict_size_trial += getsizeof(dumps(Q)) # pickle the dict and check the size
            step_count_trial += step_count
        

    # Final Route
    print("-------------------- Training Stats --------------------")
    avg_returns = r_count_trial / num_trials
    avg_steps = step_count_trial / num_trials
    avg_macs = 2 * avg_steps
    avg_bytes = dict_size_trial / num_trials

    s, done = env.reset(), False
    step = 1
    f = open(output_path, "w")
    while not done and step < 200:
        _, a = eps_greedy_action_select(Q, s, 0)
        s, r, done = env.step(a)
        f.write(str(a) + "\n")
    print(f"Avg. Steps                   : {avg_steps}")
    print(f"Avg. MACs                    : {avg_macs}") # ~2 MACs per Q learning update
    print(f"Avg. Mem Utilization (Bytes) : {avg_bytes}")
    print("--------------------------------------------------------")
    f.close()

    results = np.concatenate((avg_returns, [avg_steps], [avg_macs], [avg_bytes]))

    return results


def Q_learning_by_playthrough(num_episodes, alpha, gamma, num_trials, optimal_return, output_path):
    # 0 -> Right
    # 1 -> Up
    # 2 -> Left
    # 3 -> Down
    # 5 -> Switch Focus
    
    # Metric trackers
    r_count_trial = np.zeros(num_episodes, dtype=np.float64)
    step_count_trial = 0
    dict_size_trial = 0
    
    for t in range(num_trials):
        print(f'Starting trial {t}...')
        Q = [{}, {}, {}, {}, {}]
        early_stop_buffer = np.ones(10, dtype=np.float64) * -1000
        converged = False
        step_count = 0
        for e in range(num_episodes):
            level = 1
            env, _ = get_env(level)
            s, done_lvl_ten, done = env.reset(), False, False
            r_ep = 0
            while not done_lvl_ten:
                _, a = eps_greedy_action_select(Q, s)
                s_prime, r, done = env.step(a)
                Q_prime, _ = eps_greedy_action_select(Q, s_prime, eps=0)
                Q[a][s] = Q[a][s] + alpha * (r + gamma * Q_prime - Q[a][s])
                if done and (level != 10):
                    # transition to the next level if the agent finished the current level and
                    # the current level was not level ten
                    level += 1
                    env, _ = get_env(level)
                    s, done_lvl_ten, done = env.reset(), False, False
                elif done and (level == 10):
                    # signal that we are completely finished if the agent finished the current level
                    # and the agent is on level ten
                    done_lvl_ten = True
                else:
                    # update s to s_prime on all other transitions
                    s = s_prime
                r_ep += r
                step_count_trial += 1
            # update the metric trackers with the results of the episode
            r_count_trial[e] += r_ep
            early_stop_buffer[e % 10] = validate_playthrough(Q)
            if (not converged) and (np.mean(early_stop_buffer) == optimal_return):
                converged = True
                print('Agent has converged to the optimal solution for this level...')
                dict_size_trial += getsizeof(dumps(Q)) # pickle the dict and check the size
                step_count_trial += step_count
        
        # if the agent did not reach early stopping save the stats still
        if not converged:
            print('Agent did not meet the standards for convergence...')
            dict_size_trial += getsizeof(dumps(Q)) # pickle the dict and check the size
            step_count_trial += step_count
        
    # Final Route
    print("-------------------- Training Stats --------------------")
    avg_returns = r_count_trial / num_trials
    avg_steps = step_count_trial / num_trials
    avg_macs = 2 * avg_steps
    avg_bytes = dict_size_trial / num_trials

    level = 1
    env, _ = get_env(level)
    s, done_lvl_ten, done = env.reset(), False, False
    step = 1
    f = open(output_path, "w")
    while not done_lvl_ten and step < 1000:
        _, a = eps_greedy_action_select(Q, s, 0)
        s, r, done = env.step(a)
        step += 1
        f.write(str(a) + "\n")
        if done and (level != 10):
            # transition to the next level if the agent finished the current level and the current level was not level ten
            level += 1
            env, _ = get_env(level)
            s, done_lvl_ten, done = env.reset(), False, False
        elif done and (level == 10):
            # signal that we are completely finished if the agent finished the current level and the agent is on level ten
            done_lvl_ten = True

    print(f"Avg. Steps                   : {avg_steps}")
    print(f"Avg. MACs                    : {avg_macs}") # ~2 MACs per Q learning update
    print(f"Avg. Mem Utilization (Bytes) : {avg_bytes}")
    print("--------------------------------------------------------")
    f.close()

    results = np.concatenate((avg_returns, [avg_steps], [avg_macs], [avg_bytes]))

    return results


if __name__ == "__main__":
    args = parse()

    print("Args: ", args)
    
    if args.mode == "single_level":
        print(f'Starting training for level {args.level}...')
        env, optimal_return = get_env(args.level)
        output_path = args.output_dir + f'/level-{args.level}.res'
        r_list = Q_learning(env, args.num_episodes, args.alpha, args.gamma, args.num_trials, optimal_return, output_path)
        np.save(output_path[:-4], r_list)
        print()
    elif args.mode == "by_level":
        for level in range(1, 11):
            print(f'Starting training for level {level}...')
            env, optimal_return = get_env(level)
            output_path = args.output_dir + f'/level-{level}.res'
            r_list = Q_learning(env, args.num_episodes, args.alpha, args.gamma, args.num_trials, optimal_return, output_path)
            np.save(output_path[:-4], r_list)
            print()
    elif args.mode == "by_playthrough":
        output_path = args.output_dir + '/by-playthrough.res'
        r_list = Q_learning_by_playthrough(args.num_episodes, args.alpha, args.gamma, args.num_trials, -275, output_path)
        np.save(output_path[:-4], r_list)
        
    