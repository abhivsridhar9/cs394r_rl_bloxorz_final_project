import gym
import numpy as np
from .block import Block
from .level import Level


class LevelOne(Level):
    metadata = {"render_modes": [], "render_fps": 0}

    def __init__(self, start_pos:tuple,base_env:np.array([]),render_mode=None,):
        super().__init__(start_pos,base_env)



        # Numeric to grid mapping:
        #  9 -> out of bounds
        #  0 -> normal tile
        #  4 -> goal
        #  8 -> block

        #  20 x 10 grid (with padding)


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

        # check if the agent is out of bounds -> reset to the start
        r1, c1, r2, c2 = self.block.get_coords()

        reward,done=self._isDone(r1,c1,r2,c2)

        self._moveToStart(r1,c1,r2,c2)

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


