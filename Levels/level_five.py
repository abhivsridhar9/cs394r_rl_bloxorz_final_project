import gym
import numpy as np
from .block import Block
from .level import Level


class LevelFive(Level):

    def __init__(
        self,
        start_pos: tuple,
        base_env: np.array([]),
        render_mode=None,
    ):
        super().__init__(start_pos, base_env)

        # Numeric to grid mapping:
        #  9 -> out of bounds
        #  0 -> normal tile
        #  4 -> goal
        #  8 -> block
        #  2 -> circle ("soft") switch ... activates when landing on it any way
        #  3 -> x ("hard") switch ... activates when landing on it upright

    def step(self, action):
        # update the agent's coords by passing it the action
        self._perform_action(action)

        # check if the agent is out of bounds -> reset to the start
        r1, c1, r2, c2 = self._block.get_coords()

        reward, done = self._is_done(r1,c1,r2,c2)

        self._move_to_start(r1,c1,r2,c2)
        self._toggle_circle_switches(r1, c1, r2, c2, np.array([(2, 7), (2, 8)]))
        self._toggle_circle_switches(r1, c1, r2, c2, np.array([(2, 7), (2, 8)]))

        state = self._format_environment()

        return state, reward, done
