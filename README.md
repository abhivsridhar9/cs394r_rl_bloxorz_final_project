# Introduction
This code base was developed for a project in CS394R at The University of Texas at Austin. It uses Q-learning and Deep Q-networks to train agents to play the puzzle flash game Bloxorz (https://bloxorz.io/). Below we detail the contents of each file, as well as how to use the code yourself.

# Repository Structure
* `/tabularQ.py`: This is the main script used to train agents using Q-learning.
* `/bot.py`: This script takes the output from `tabularQ.py` and uses it to play Bloxorz.
* `/block.py`: This script contains the class definition for the Bloxorz prism, which controls movement and focus.
* `/plot.py`: Using the contents of `/results` this script generates several plots that are dumped into `/figs`.
* `/DQN`: This directory contains four notebooks that have been adapted from https://github.com/Curt-Park/rainbow-is-all-you-need. These notebooks implement training Bloxorz agents using a variety of DQNs.
* `/levels`: This directory contains the class definition for the environment as well as a config file for configuring the environment for different Bloxorz levels.
* `/figs`: This directory contains the results from the `plot.py` script.
* `/results`: This directory contains the results from the `tabularQ.py` and `/DQN` scripts. This includes training metrics as well as the final training trajectory of the agent.

# Setting Up the Python Environment
This code was developed using Python version 3.10.8. Set up a virtual environment and then use the accompanying `requirements.txt` file.

`pip install -r requirements.txt`

# Running Q-Learning
### Single Level
`python tabularQ.py --mode single_level --num_episodes 2000 --num_trials 25 --level 1`

### By-Level
`python tabularQ.py --mode by_level --num_episodes 2000 --num_trials 25`

### By-Playthrough
`python tabularQ.py --mode by_playthrough --num_episodes 2000 --num_trials 25`

# Running the Bot
Currently only single level mode is supported for the bot.

`python bot.py --model single_level --input_file ./results/level-1.res`

# Running Deep Q-Networks
Simply open a notebook and press "Run All".

# Code References
The portion of the code contained under the `/DQN` directory was adapted from https://github.com/Curt-Park/rainbow-is-all-you-need.
