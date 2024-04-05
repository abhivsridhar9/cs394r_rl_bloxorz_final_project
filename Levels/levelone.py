import gym
import numpy as np
import block


class LevelOne(gym.Env):
    metadata = {"render_modes": [], "render_fps": 0}

    def __init__(self, render_mode=None):

        self.block = Block(3, 6, 3, 6)

        # Numeric to grid mapping:
        # -1 -> out of bounds
        #  0 -> normal tile
        #  4 -> goal
        #  8 -> block

        #  20 x 10 grid (with padding)
        self.base_env = np.ndarray(
            [
                [-1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1,-1, -1, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1,-1, -1, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1,-1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1,-1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1],
                [-1, -1, -1,-1, -1, -1, -1, -1, -1, -1, 0, 0, 4, 0, 0, -1, -1, -1, -1, -1],
                [-1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            ]
        )

        pass

    def _get_obs(self):
        return {"agent": self._agent_location, "target": self._target_location}

    def reset(self):
        # set both of the agent's coords to (3, 6) and (3, 6)
        self.block.set_coords(3, 6, 3, 6)

        # reset the environment (important to undo any obstacle interactions)
        self.current_env = self.base_env

        # place the agent in the environment using its position
        state = np.copy(self.current_env)
        state[3, 6] = 8
        state = state.ravel()

        return state

    def step(self, action):
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
        x1, y1, x2, y2 = self.block.get_coords()
        if self.current_env[x1, y1] == -1 or self.current_env[x2, y2] == -1:
            # TODO: some levels may not reset when you fall off, hence manually resetting the block coordinates
            self.block.set_coords(3, 6, 3, 6)

        # check if the agent is on a button -> change the current_env to reflect this

        # check if the agent is on the goal -> set done to True and reward to 0
        if self.current_env[x1, y1] == 4 and self.current_env[x2, y2] == 4:
            reward = 0
            done = True

        # place the agent in the environment using its position
        x1, y1, x2, y2 = self.block.get_coords()
        state = np.copy(self.current_env)
        state[x1, y1] = 8
        state[x2, y2] = 8
        state = state.ravel()

        return state, reward, done
