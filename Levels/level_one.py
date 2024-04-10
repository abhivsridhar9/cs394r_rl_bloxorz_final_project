import gym
import numpy as np
from .block import Block
from .level import Level


class LevelOne(Level):

    def __init__(
        self,
        start_pos: tuple,
        base_env: np.array([]),
        render_mode=None,
    ):
        super().__init__(start_pos, base_env)

    def step(self, action):
        # update the agent's coords by passing it the action

        self._perform_action(action)

        # check if the agent is out of bounds -> reset to the start
        r1, c1, r2, c2 = self.block.get_coords()

        reward, done = self._is_done(r1, c1, r2, c2)

        self._move_to_start(r1, c1, r2, c2)

        state = self._format_environment()

        return state, reward, done
