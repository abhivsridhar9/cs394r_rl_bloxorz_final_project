import matplotlib.pyplot as plt
import numpy as np

level_one_res = np.load('./results/level-1.npy')
level_two_res = np.load('./results/level-2.npy')
level_three_res = np.load('./results/level-3.npy')
level_four_res = np.load('./results/level-4.npy')
level_five_res = np.load('./results/level-5.npy')
level_six_res = np.load('./results/level-6.npy')
level_seven_res = np.load('./results/level-7.npy')
level_eight_res = np.load('./results/level-8.npy')
level_nine_res = np.load('./results/level-9.npy')
level_ten_res = np.load('./results/level-10.npy')
by_playthrough_res = np.load('./results/by-playthrough.npy')

level_one = {
    'label': 'Level 1',
    'avg_returns': level_one_res[:-3],
    'avg_steps': level_one_res[-3],
    'avg_macs': level_one_res[-2],
    'avg_mem': level_one_res[-1]
}

level_two = {
    'label': 'Level 2',
    'avg_returns': level_two_res[:-3],
    'avg_steps': level_two_res[-3],
    'avg_macs': level_two_res[-2],
    'avg_mem': level_two_res[-1]
}

level_three = {
    'label': 'Level 3',
    'avg_returns': level_three_res[:-3],
    'avg_steps': level_three_res[-3],
    'avg_macs': level_three_res[-2],
    'avg_mem': level_three_res[-1]
}

level_four = {
    'label': 'Level 4',
    'avg_returns': level_four_res[:-3],
    'avg_steps': level_four_res[-3],
    'avg_macs': level_four_res[-2],
    'avg_mem': level_four_res[-1]
}

level_five = {
    'label': 'Level 5',
    'avg_returns': level_five_res[:-3],
    'avg_steps': level_five_res[-3],
    'avg_macs': level_five_res[-2],
    'avg_mem': level_five_res[-1]
}

level_six = {
    'label': 'Level 6',
    'avg_returns': level_six_res[:-3],
    'avg_steps': level_six_res[-3],
    'avg_macs': level_six_res[-2],
    'avg_mem': level_six_res[-1]
}

level_seven = {
    'label': 'Level 7',
    'avg_returns': level_seven_res[:-3],
    'avg_steps': level_seven_res[-3],
    'avg_macs': level_seven_res[-2],
    'avg_mem': level_seven_res[-1]
}

level_eight = {
    'label': 'Level 8',
    'avg_returns': level_eight_res[:-3],
    'avg_steps': level_eight_res[-3],
    'avg_macs': level_eight_res[-2],
    'avg_mem': level_eight_res[-1]
}

level_nine = {
    'label': 'Level 9',
    'avg_returns': level_nine_res[:-3],
    'avg_steps': level_nine_res[-3],
    'avg_macs': level_nine_res[-2],
    'avg_mem': level_nine_res[-1]
}

level_ten = {
    'label': 'Level 10',
    'avg_returns': level_ten_res[:-3],
    'avg_steps': level_ten_res[-3],
    'avg_macs': level_ten_res[-2],
    'avg_mem': level_ten_res[-1]
}

by_playthrough = {
    'label': 'By-Playthrough',
    'avg_returns': by_playthrough_res[:-3],
    'avg_steps': by_playthrough_res[-3],
    'avg_macs': by_playthrough_res[-2],
    'avg_mem': by_playthrough_res[-1]
}


q_learning = [level_one, level_two, level_three, level_four, level_five, level_six,
              level_seven, level_eight, level_nine, level_ten]

aggregate_by_level = {
    'label': 'Agg. By-Level',
    'avg_returns': np.sum(np.array([x['avg_returns'] for x in q_learning]), axis=0),
    'avg_steps': sum([x['avg_steps'] for x in q_learning]),
    'avg_macs': sum([x['avg_macs'] for x in q_learning]),
    'avg_mem': sum([x['avg_mem'] for x in q_learning])
}

q_learning.append(aggregate_by_level)
q_learning.append(by_playthrough)

labels = [x['label'] for x in q_learning]
steps = [x['avg_steps'] for x in q_learning]
macs = [x['avg_macs'] for x in q_learning]
mem = [x['avg_mem'] for x in q_learning]

# plot steps
fig, ax = plt.subplots(figsize=(15,10))
ax.bar(labels, steps, width=0.8)
ax.set_title('Average Number of Steps to Optimal Solution')
ax.set_yscale('log')
ax.set_ylabel('Steps')
ax.grid()
for tick in ax.get_xticklabels():
    tick.set_rotation(30)
plt.savefig('./figs/steps.pdf')
plt.clf()

# plot macs
fig, ax = plt.subplots(figsize=(15,10))
ax.bar(labels, macs, width=0.8)
ax.set_title('Average Number of MACs for Optimal Solution')
ax.set_yscale('log')
ax.set_ylabel('MACs')
ax.grid()
for tick in ax.get_xticklabels():
    tick.set_rotation(30)
plt.savefig('./figs/macs.pdf')
plt.clf()

# plot mem
fig, ax = plt.subplots(figsize=(15,10))
ax.bar(labels, mem, width=0.8)
ax.set_title('Average Number of Byte-Storage for Optimal Solution')
ax.set_yscale('log')
ax.set_ylabel('Bytes')
ax.grid()
for tick in ax.get_xticklabels():
    tick.set_rotation(30)
plt.savefig('./figs/bytes.pdf')
plt.clf()

# plot returns
fig, ax = plt.subplots(figsize=(15,10))
for x in q_learning:
    ax.plot(np.clip(x['avg_returns'], a_min=-2000, a_max=0), label=x['label'])
ax.grid()
ax.legend()
ax.set_title('Average Training Returns')
ax.set_xlabel('Episode')
ax.set_ylabel('Average Return')
plt.savefig('./figs/q_learning_returns.pdf')

# dqn plots
dqn_res = np.load('./results/dqn.npy')
double_dqn_res = np.load('./results/double_dqn.npy')
per_dqn_res = np.load('./results/per_dqn.npy')

dqn = {
    'label': 'DQN',
    'avg_steps': dqn_res[-1],
    'avg_mem': 1480000,
    'avg_macs': 780000 * dqn_res[-1]
}

double_dqn = {
    'label': 'Double DQN',
    'avg_steps': double_dqn_res[-1],
    'avg_mem': 1480000,
    'avg_macs': 780000 * double_dqn_res[-1]
}

per_dqn = {
    'label': 'Prioritized Replay',
    'avg_steps': per_dqn_res[-1],
    'avg_mem': 1480000,
    'avg_macs': 780000 * per_dqn_res[-1]
}

level_one['label'] = 'Q-Learning'
dqns = [level_one, dqn, double_dqn, per_dqn]

labels = [x['label'] for x in dqns]
steps = [x['avg_steps'] for x in dqns]
macs = [x['avg_macs'] for x in dqns]
mem = [x['avg_mem'] for x in dqns]

fig, ax = plt.subplots(figsize=(15,10))
ax.bar(labels, steps, width=0.8)
ax.set_title('Average Number of Steps to Optimal Solution on Level One')
ax.set_yscale('log')
ax.set_ylabel('Steps')
ax.grid()
for tick in ax.get_xticklabels():
    tick.set_rotation(30)
plt.savefig('./figs/dqn_steps.pdf')
plt.clf()

fig, ax = plt.subplots(figsize=(15,10))
ax.bar(labels, macs, width=0.8)
ax.set_title('Average Number of MACs for Optimal Solution on Level One')
ax.set_yscale('log')
ax.set_ylabel('MACs')
ax.grid()
for tick in ax.get_xticklabels():
    tick.set_rotation(30)
plt.savefig('./figs/dqn_macs.pdf')
plt.clf()

fig, ax = plt.subplots(figsize=(15,10))
ax.bar(labels, mem, width=0.8)
ax.set_title('Average Number of Byte-Storage for Optimal Solution')
ax.set_yscale('log')
ax.set_ylabel('Bytes')
ax.grid()
for tick in ax.get_xticklabels():
    tick.set_rotation(30)
plt.savefig('./figs/dqn_bytes.pdf')
plt.clf()

