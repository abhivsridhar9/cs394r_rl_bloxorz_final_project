from abc import ABC, abstractmethod
import gym
import numpy as np
from .block import Block

class Level(gym.Env,ABC):

    def __init__(self,start_pos:tuple,base_env:np.array([]),render_mode=None):
        self.r_start=start_pos[0]
        self.c_start=start_pos[1]

        self.block = Block(self.r_start,self.c_start,self.r_start,self.c_start)

        self.base_env=base_env

    @abstractmethod
    def step(self):
        raise NotImplementedError

    def reset(self):
        # set both of the agent's coords to (self.r_start,self.c_start) and (self.r_start,self.c_start)
        self.block.set_coords(self.r_start,self.c_start,self.r_start,self.c_start)

        # reset the environment (important to undo any obstacle interactions)
        self.current_env = self.base_env

        # place the agent in the environment using its position
        state = np.copy(self.current_env)
        state[self.r_start,self.c_start] = 8
        state = state.ravel()
        state = np.array2string(state, separator='')

        return state

    def _moveToStart(self,r1,c1,r2,c2):
            if self.current_env[r1, c1] == 9 or self.current_env[r2, c2] == 9:
                # TODO: some levels may not reset when you fall off, hence manually resetting the block coordinates
                self.block.set_coords(self.r_start,self.c_start,self.r_start,self.c_start)

    def _isDone(self,r1,c1,r2,c2):
            # check if the agent is on the goal -> set done to True and reward to 0

            # reward is -1 and done is False unless the agent hit the goal
            reward =-1
            done =False

            if self.current_env[r1, c1] == 4 and self.current_env[r2, c2] == 4:
                reward = 0
                done = True


            return reward,done

    def get_state(self):
        r1, c1, r2, c2 = self.block.get_coords()
        print(r1, c1, r2, c2)
        state = np.copy(self.current_env)
        state[r1, c1] = 8
        state[r2, c2] = 8

        return state