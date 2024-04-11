import gym
import numpy as np
from block import Block


class Level(gym.Env):
    metadata = {"render_modes": [], "render_fps": 0}

    def __init__(
        self,
        start_pos: tuple,
        base_env: np.array([]),
        soft_switches=np.array([]),
        hard_switches=np.array([]),
        teleport_switches=np.array([]),
        render_mode=None,
    ):
        self._r_start = start_pos[0]
        self._c_start = start_pos[1]

        self._block = Block(self._r_start, self._c_start, self._r_start, self._c_start)

        self._base_env = base_env

        self._soft_switches = soft_switches
        self._hard_switches = hard_switches
        self._teleport_switches = teleport_switches

        self._actions = {
            0: self._block.move_right,
            1: self._block.move_up,
            2: self._block.move_left,
            3: self._block.move_down,
            4: self._block.set_focus_block,
        }

    def step(self, action):
        # if the block is split, check if single blocks are adjacent, and join together
        self._block.join_single_blocks()

        # update the agent's coords by passing it the action
        self._perform_action(action)

        # check if the agent is out of bounds -> reset to the start
        r1, c1, r2, c2 = self._block.get_coords()

        reward, done = self._is_done(r1, c1, r2, c2)

        # only check for environment changes if the action is not "Switch Focus"
        if action != 4:
            self._move_to_start(r1, c1, r2, c2)
            self._activate_teleport_switch(r1,c1,r2,c2)
            self._toggle_soft_switches(r1, c1, r2, c2)
            self._toggle_hard_switches(r1, c1, r2, c2)

        state = self._format_environment()

        return state, reward, done

    def reset(self):
        # set both of the agent's coords to (self._r_start,self._c_start) and (self._r_start,self._c_start)
        self._block.set_coords(
            self._r_start, self._c_start, self._r_start, self._c_start
        )

        # reset the environment (important to undo any obstacle interactions)
        self._current_env = np.copy(self._base_env)

        # place the agent in the environment using its position
        state = np.copy(self._current_env)
        state[self._r_start, self._c_start] = 8
        state = state.ravel()
        state = np.array2string(state, separator="")

        return state

    def _move_to_start(self, r1, c1, r2, c2):
        if self._current_env[r1, c1] == 9 or self._current_env[r2, c2] == 9:
            self.reset()

    def _is_done(self, r1, c1, r2, c2):
        # check if the agent is on the goal -> set done to True and reward to 0

        # reward is -1 and done is False unless the agent hit the goal
        reward = -1
        done = False

        if self._current_env[r1, c1] == 4 and self._current_env[r2, c2] == 4:
            reward = 0
            done = True

        return reward, done

    def _format_environment(self):
        # place the agent in the environment using its position
        r1, c1, r2, c2 = self._block.get_coords()
        state = np.copy(self._current_env)
        state[r1, c1] = 8
        state[r2, c2] = 8

        state = state.ravel()
        state = np.array2string(state, separator="")

        return state

    def _toggle_soft_switches(self, r1, c1, r2, c2):
        # check if the agent is on a circle switch -> activate bridge
        for c in self._soft_switches:
            switch_location = c["switch_location"]
            toggle_tiles = c["toggle_tiles"]
            mode = c["mode"]

            if (r1 == switch_location[0] and c1 == switch_location[1]) or (
                r2 == switch_location[0] and c2 == switch_location[1]
            ):
                if mode == "toggle":
                    if self._current_env[toggle_tiles[0][0], toggle_tiles[0][1]] == 0:
                        for t in toggle_tiles:
                            self._current_env[t[0], t[1]] = 9
                            self._current_env[t[0], t[1]] = 9

                    else:
                        for t in toggle_tiles:
                            self._current_env[t[0], t[1]] = 0
                            self._current_env[t[0], t[1]] = 0
                elif mode == "on":
                    for t in toggle_tiles:
                        self._current_env[t[0], t[1]] = 0
                        self._current_env[t[0], t[1]] = 0
                elif mode == "off":
                    for t in toggle_tiles:
                        self._current_env[t[0], t[1]] = 9
                        self._current_env[t[0], t[1]] = 9

    def _toggle_hard_switches(self, r1, c1, r2, c2):
        # check if the agent is on an x switch -> activate bridge
        for c in self._hard_switches:
            switch_location = c["switch_location"]
            toggle_tiles = c["toggle_tiles"]

            if (r1 == switch_location[0] and c1 == switch_location[1]) and (
                r2 == switch_location[0] and c2 == switch_location[1]
            ):
                if self._current_env[toggle_tiles[0][0], toggle_tiles[0][1]] == 0:
                    for t in toggle_tiles:
                        self._current_env[t[0], t[1]] = 9
                        self._current_env[t[0], t[1]] = 9

                else:
                    for t in toggle_tiles:
                        self._current_env[t[0], t[1]] = 0
                        self._current_env[t[0], t[1]] = 0


    def _activate_teleport_switch(self,r1,c1,r2,c2):
        # check if block is on teleport switch -> split block into two single blocks
        for t in self._teleport_switches:
            switch_location = c["switch_location"]
            split_positions = c["split_positions"]

            if (r1 == switch_location[0] and c1 == switch_location[1]) and (
                r2 == switch_location[0] and c2 == switch_location[1]
            ):

                single_block_one=split_positions[0]
                single_block_two=split_positions[2]

                r1=single_block_one[0]
                c1=single_block_one[1]

                r2=single_block_two[0]
                c2=single_block_two[0]

                self._block.set_focus_block(1)



    def _handle_orange_tile(self, r1, c1, r2, c2):
        # check if block is vertical
        if (r1, c1) == (r2, c2):
            # check if tile is orange tile
            if self._current_env[r1, c1] == 1:
                # tile disappears/block falls through grid

                self._block.set_coords(
                    self._r_start, self._c_start, self._r_start, self._c_start
                )

        # nothing happens if block is not vertical on an orange tile
        return state

    def _perform_action(self, action):
        # Get the corresponding method from 'actions' and call it
        action_method = self._actions.get(action)
        if action_method:
            action_method()
        else:
            print("Invalid action")

    def get_state(self):
        r1, c1, r2, c2 = self._block.get_coords()
        print(r1, c1, r2, c2)
        state = np.copy(self._current_env)
        state[r1, c1] = 8
        state[r2, c2] = 8
