import gym
import numpy as np
import block


class LevelTwo(gym.Env):
    metadata = {"render_modes": [], "render_fps": 0}

    def __init__(self, render_mode=None):

        self.block = Block(6, 5, 6, 5)

        # Numeric to grid mapping:
        # -1 -> out of bounds
        #  0 -> normal tile
        #  4 -> goal
        #  8 -> block
        #  2 -> circle ("soft") switch ... activates when landing on it any way
        #  3 -> x ("hard") switch ... activates when landing on it upright

        #  20 x 10 grid (with padding)
        self.base_env = np.ndarray(
            [
                [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                [-1,-1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                [-1,-1,-1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, -1, -1, 0, 0, 0, -1, -1, -1],
                [-1,-1,-1, -1, 0, 0, 0, 0, -1, -1, 0, 0, 3, 0, -1, -1, 0, 4, 0, -1, -1, -1],
                [-1,-1,-1, -1, 0, 0, 2, 0, -1, -1, 0, 0, 0, 0, -1, -1, 0, 0, 0, -1, -1, -1],
                [-1,-1,-1, -1, 0, 0, 0, 0, -1, -1, 0, 0, 0, 0, -1, -1, 0, 0, 0, -1, -1, -1],
                [-1,-1,-1, -1, 0, 0, 0, 0, -1, -1, 0, 0, 0, 0, -1, -1, 0, 0, 0, -1, -1, -1],
                [-1,-1,-1, -1, 0, 0, 0, 0, -1, -1, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            ]
        )

        pass

    def _get_obs(self):
        return {"agent": self._agent_location, "target": self._target_location}

    def reset(self):
        # set both of the agent's coords to (6, 5) and (6, 5)
        self.block.set_coords(6, 5, 6, 5)

        # reset the environment (important to undo any obstacle interactions)
        self.current_env = self.base_env

        # place the agent in the environment using its position
        state = np.copy(self.current_env)
        state[6, 5] = 8
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
        r1, c1, r2, c2 = self.block.get_coords()
        if self.current_env[r1, c1] == -1 or self.current_env[r2, c2] == -1:
            # TODO: some levels may not reset when you fall off, hence manually resetting the block coordinates
            self.block.set_coords(6, 5, 6, 5)

        # check if the agent is on a circle switch -> activate bridge
        if self.current_env[r1, c1] == 2 or self.current_env[r2, c2] == 2:
            if self.current_env[6,8]==0 and self.current_env[6,9]==0:
                elf.current_env[6,8]==-1
                elf.current_env[6,9]==-1

            else:
                elf.current_env[6,8]==0
                elf.current_env[6,9]==0

        # check if the agent is on an x switch -> activate brigge
        if self.current_env[r1, c1] == 3 and self.current_env[r2, c2] == 3:
            if self.current_env[6,12]==0 and self.current_env[6,13]==0:
                elf.current_env[6,12]==-1
                elf.current_env[6,13]==-1

            else:
                elf.current_env[6,12]==0
                elf.current_env[6,13]==0

        # check if the agent is on the goal -> set done to True and reward to 0
        if self.current_env[r1, c1] == 4 and self.current_env[r2, c2] == 4:
            reward = 0
            done = True

        # place the agent in the environment using its position
        r1, c1, r2, c2 = self.block.get_coords()
        state = np.copy(self.current_env)
        state[r1, c1] = 8
        state[r2, c2] = 8
        state = state.ravel()

        return state, reward, done
