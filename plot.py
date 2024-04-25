import matplotlib.pyplot as plt
import numpy as np

level_one = {
    'label': 'Level 1',
    'avg_steps': 9640.16,
    'avg_macs': 19280.32,
    'avg_mem': 27136.16
}

level_two = {
    'label': 'Level 2',
    'avg_steps': 129448.96,
    'avg_macs': 258897.92,
    'avg_mem': 117451.0
}

level_three = {
    'label': 'Level 3',
    'avg_steps': 56652.0,
    'avg_macs': 113304.0,
    'avg_mem': 35961.76
}

level_four = {
    'label': 'Level 4',
    'avg_steps': 101956.6,
    'avg_macs': 203913.2,
    'avg_mem': 43947.0
}

level_five = {
    'label': 'Level 5',
    'avg_steps': 283958.08,
    'avg_macs': 567916.16,
    'avg_mem': 112393.76
}

level_six = {
    'label': 'Level 6',
    'avg_steps': 106430.08,
    'avg_macs': 212860.16,
    'avg_mem': 35403.36
}

level_seven = {
    'label': 'Level 7',
    'avg_steps': 268046.76,
    'avg_macs': 536093.52,
    'avg_mem': 57974.48
}

level_eight = {
    'label': 'Level 8',
    'avg_steps': 233825.36,
    'avg_macs': 467650.72,
    'avg_mem': 438552.6
}

level_nine = {
    'label': 'Level 9',
    'avg_steps': 761178.92,
    'avg_macs': 1522357.84,
    'avg_mem': 495155.6
}

level_ten = {
    'label': 'Level 10',
    'avg_steps': 8429739.96,
    'avg_macs': 16859479.92,
    'avg_mem': 2556735.76
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