from abc import ABC, abstractmethod
import gym
import numpy as np
from .block import Block


class Level(gym.Env, ABC):
    metadata = {"render_modes": [], "render_fps": 0}

    def __init__(self, start_pos: tuple, base_env: np.array([]), circle_switches=None,x_switches=None,render_mode=None):
        self.r_start = start_pos[0]
        self.c_start = start_pos[1]

        self.block = Block(self.r_start, self.c_start, self.r_start, self.c_start)

        self.base_env = base_env

        self.circle_switches=circle_switches
        self.x_switches=x_switches

        self.action_map = {
            0: self.block.move_right,
            1: self.block.move_up,
            2: self.block.move_left,
            3: self.block.move_down,
        }

    @abstractmethod
    def step(self):
        raise NotImplementedError

    def reset(self):
        # set both of the agent's coords to (self.r_start,self.c_start) and (self.r_start,self.c_start)
        self.block.set_coords(self.r_start, self.c_start, self.r_start, self.c_start)

        # reset the environment (important to undo any obstacle interactions)
        self.current_env = self.base_env

        # place the agent in the environment using its position
        state = np.copy(self.current_env)
        state[self.r_start, self.c_start] = 8
        state = state.ravel()
        state = np.array2string(state, separator="")

        return state

    def _move_to_start(self, r1, c1, r2, c2):
        if self.current_env[r1, c1] == 9 or self.current_env[r2, c2] == 9:
            # TODO: some levels may not reset when you fall off, hence manually resetting the block coordinates
            self.block.set_coords(
                self.r_start, self.c_start, self.r_start, self.c_start
            )

    def _is_done(self, r1, c1, r2, c2):
        # check if the agent is on the goal -> set done to True and reward to 0

        # reward is -1 and done is False unless the agent hit the goal
        reward = -1
        done = False

        if self.current_env[r1, c1] == 4 and self.current_env[r2, c2] == 4:
            reward = 0
            done = True

        return reward, done

    def _format_environment(self):
        # place the agent in the environment using its position
        r1, c1, r2, c2 = self.block.get_coords()
        state = np.copy(self.current_env)
        state[r1, c1] = 8
        state[r2, c2] = 8

        state = state.ravel()
        state = np.array2string(state, separator="")

        return state

    def _toggle_circle_switch(self, r1, c1, r2, c2, toggle_tiles: np.array([tuple])):

        # check if the agent is on a circle switch -> activate bridge
        if self.current_env[r1, c1] == 2 or self.current_env[r2, c2] == 2:

            if self.current_env[toggle_tiles[0][0], toggle_tiles[0][1]] == 0:
                for t in toggle_tiles:
                    self.current_env[t[0], t[1]] = 9
                    self.current_env[t[0], t[1]] = 9

            else:
                for t in toggle_tiles:
                    self.current_env[t[0], t[1]] = 0
                    self.current_env[t[0], t[1]] = 0

    def _toggle_x_switch(self, r1, c1, r2, c2, toggle_tiles: np.array([tuple])):
        # check if the agent is on an x switch -> activate bridge
        if self.current_env[r1, c1] == 3 and self.current_env[r2, c2] == 3:

            if self.current_env[toggle_tiles[0][0], toggle_tiles[0][1]] == 0:
                for t in toggle_tiles:
                    self.current_env[t[0], t[1]] = 9
                    self.current_env[t[0], t[1]] = 9

            else:
                for t in toggle_tiles:
                    self.current_env[t[0], t[1]] = 0
                    self.current_env[t[0], t[1]] = 0

    def get_state(self):
        r1, c1, r2, c2 = self.block.get_coords()
        print(r1, c1, r2, c2)
        state = np.copy(self.current_env)
        state[r1, c1] = 8
        state[r2, c2] = 8

        return state


    def _perform_action(self, action):
        # Get the corresponding method from 'action_map' and call it
        action_method = self.action_map.get(action)
        if action_method:
            action_method()
        else:
            print("Invalid action")
