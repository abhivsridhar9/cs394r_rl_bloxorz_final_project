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
# by_playthrough_res = np.load('./results/by-playthrough.npy')

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

aggregate_by_level = {
    'label': 'Agg. By-Level',
    'avg_steps': 10487306.96,
    'avg_macs': 20974613.92,
    'avg_mem': 3920711.48
}

by_playthrough = {
    'label': 'By-Playthrough',
    'avg_steps': 12607142.92,
    'avg_macs': 25214285.84,
    'avg_mem': 3932260.52
}

q_learning = [level_one, level_two, level_three, level_four, level_five, level_six,
              level_seven, level_eight, level_nine, level_ten, aggregate_by_level, by_playthrough]


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