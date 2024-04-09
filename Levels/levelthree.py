import gym
import numpy as np
from .block import Block


class LevelThree(gym.Env):
    metadata = {"render_modes": [], "render_fps": 0}

    def __init__(self, render_mode=None):

        self.block = Block(4, 3, 4, 3)

        # Numeric to grid mapping:
        #  9 -> out of bounds
        #  0 -> normal tile
        #  4 -> goal
        #  8 -> block

        #  20 x 10 grid (with padding)
        self.base_env = np.array(
            [
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9, 9, 9],
                [9, 9, 0, 0, 0, 0, 9, 9, 0, 0, 0, 9, 9, 0, 0, 9, 9, 9, 9, 9],
                [9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 0, 0, 0, 0, 9, 9, 9],
                [9, 9, 0, 0, 0, 0, 9, 9, 9, 9, 9, 9, 9, 0, 0, 4, 0, 9, 9, 9],
                [9, 9, 0, 0, 0, 0, 9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 0, 9, 9, 9],
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 9, 9, 9],
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
            ]
        )

    def reset(self):
        # set both of the agent's coords to (4, 3) and (4, 3)
        self.block.set_coords(4, 3, 4, 3)

        # reset the environment (important to undo any obstacle interactions)
        self.current_env = self.base_env

        # place the agent in the environment using its position
        state = np.copy(self.current_env)
        state[4, 3] = 8
        state = state.ravel()
        state = np.array2string(state, separator='')

        return state

    def step(self, action,final_route):
        # update the agent's coords by passing it the action
        match action:
            case 0:
                self.block.moveRight()
            case 1:
                self.block.moveUp()
            case 2:
                self.block.moveLeft()
            case 3:
                self.block.moveDown()

        # reward is -1 and done is False unless the agent hit the goal
        reward = -1
        done = False

        # check if the agent is out of bounds -> reset to the start
        r1, c1, r2, c2 = self.block.get_coords()
        if self.current_env[r1, c1] == 9 or self.current_env[r2, c2] == 9:
            # TODO: some levels may not reset when you fall off, hence manually resetting the block coordinates
            self.block.set_coords(4, 3, 4, 3)

        # check if the agent is on a button -> change the current_env to reflect this

        # check if the agent is on the goal -> set done to True and reward to 0
        if self.current_env[r1, c1] == 4 and self.current_env[r2, c2] == 4:
            reward = 0
            done = True

        # place the agent in the environment using its position
        r1, c1, r2, c2 = self.block.get_coords()
        state = np.copy(self.current_env)
        state[r1, c1] = 8
        state[r2, c2] = 8

        if final_route:
            print("\nCurrent State: \n",state,"\n")

        state = state.ravel()
        state = np.array2string(state, separator='')

        return state, reward, done

    def get_state(self):
        r1, c1, r2, c2 = self.block.get_coords()
        print(r1, c1, r2, c2)
        state = np.copy(self.current_env)
        state[r1, c1] = 8
        state[r2, c2] = 8

        return state
