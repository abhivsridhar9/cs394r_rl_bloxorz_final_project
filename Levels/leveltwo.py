import gym
import numpy as np
from .block import Block


class LevelTwo(gym.Env):
    metadata = {"render_modes": [], "render_fps": 0}

    def __init__(self, render_mode=None):

        self.r_start=6
        self.c_start=3

        self.block = Block(self.r_start,self.c_start,self.r_start,self.c_start)

        # Numeric to grid mapping:
        #  9 -> out of bounds
        #  0 -> normal tile
        #  4 -> goal
        #  8 -> block
        #  2 -> circle ("soft") switch ... activates when landing on it any way
        #  3 -> x ("hard") switch ... activates when landing on it upright

        self.base_env = np.array(
            [
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 0, 9, 9, 0, 0, 0, 9, 9, 9],
                [9, 9, 0, 0, 0, 0, 9, 9, 0, 0, 3, 0, 9, 9, 0, 4, 0, 9, 9, 9],
                [9, 9, 0, 0, 2, 0, 9, 9, 0, 0, 0, 0, 9, 9, 0, 0, 0, 9, 9, 9],
                [9, 9, 0, 0, 0, 0, 9, 9, 0, 0, 0, 0, 9, 9, 0, 0, 0, 9, 9, 9],
                [9, 9, 0, 0, 0, 0, 9, 9, 0, 0, 0, 0, 9, 9, 0, 0, 0, 9, 9, 9],
                [9, 9, 0, 0, 0, 0, 9, 9, 0, 0, 0, 0, 9, 9, 9, 9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
            ]
        )



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

    def step(self, action,final_route):
        def toggleHardSwitch(toggle_tiles=np.array([tuple])):
            # check if the agent is on an x switch -> activate bridge
            if self.current_env[r1, c1] == 3 and self.current_env[r2, c2] == 3:

                if self.current_env[toggle_tiles[0][0],toggle_tiles[0][1]]==0:
                    for t in toggle_tiles:
                        self.current_env[t[0],t[1]]=9
                        self.current_env[t[0],t[1]]=9

                else:
                    for t in toggle_tiles:
                        self.current_env[t[0],t[1]]=0
                        self.current_env[t[0],t[1]]=0


        def toggleSoftSwitch(toggle_tiles=np.array([tuple])):
            # check if the agent is on a circle switch -> activate bridge
            if self.current_env[r1, c1] == 2 or self.current_env[r2, c2] == 2:

                if self.current_env[toggle_tiles[0][0],toggle_tiles[0][1]]==0:
                    for t in toggle_tiles:
                        self.current_env[t[0],t[1]]=9
                        self.current_env[t[0],t[1]]=9

                else:
                    for t in toggle_tiles:
                        self.current_env[t[0],t[1]]=0
                        self.current_env[t[0],t[1]]=0

        def moveToStart():
            if self.current_env[r1, c1] == 9 or self.current_env[r2, c2] == 9:
                # TODO: some levels may not reset when you fall off, hence manually resetting the block coordinates
                self.block.set_coords(self.r_start,self.c_start,self.r_start,self.c_start)

        def isDone():
            # check if the agent is on the goal -> set done to True and reward to 0
            reward =-1
            done =False

            if self.current_env[r1, c1] == 4 and self.current_env[r2, c2] == 4:
                reward = 0
                done = True


            return reward,done

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


        # check if the agent is out of bounds -> reset to the start
        r1, c1, r2, c2 = self.block.get_coords()

        reward,done=isDone()

        moveToStart()
        toggleSoftSwitch(np.array([(6,6),(6,7)]))
        toggleHardSwitch(np.array([(6,12),(6,13)]))


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


