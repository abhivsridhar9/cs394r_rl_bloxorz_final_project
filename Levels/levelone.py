import gym
import numpy as np

class Block():

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_coords(self):
        return self.x1, self.y1, self.x2, self.y2

    def isVertical(self):
        if self.x1==self.x2 and self.y1==self.y2:
            return True

        return False

    def isWide(self):
        if self.isVertical:
            return False

        if self.x1!=self.x2 and self.y1==self.y2:
            return  True

        return False

    def moveRight(self):
        # vertical
        if self.isVertical:
           self.x1+=1
           self.x2+=1

        # flat and wide
        elif self.isWide:
            self.x2+=1
            self.x1+=2

        # flat and long
        else:
            self.x1+=1
            self.x2+=1

    def moveLeft(self):
        # vertical
        if self.isVertical:
           self.x1-=2
           self.x2-=1

        # flat and wide
        elif self.isWide:
            self.x1-=1
            self.x2-=2

        # flat and long
        else:
            self.x1-=1
            self.x2-=1

    def moveUp(self):
       # vertical
        if self.isVertical:
            self.y1+=2
            self.y2+=1

        # flat and wide
        elif self.isWide:
            self.y1+=1
            self.y2+=1

        # flat and long
        else:
            self.y2+=2
            self.y1+=1

    def moveDown(self):
        # vertical
        if self.isVertical:
            self.y1-=1
            self.y2-=2

        # flat and wide
        elif self.isWide:
            self.y1-=1
            self.y2-=1

        # flat and long
        else:
            self.y2-=1
            self.y1-=2


class LevelOne(gym.Env):
    metadata = {"render_modes": [], "render_fps": 0}

    def __init__(self, render_mode=None):

        self.block = Block(4, 4, 4, 4)

        # Numeric to grid mapping:
        # -1 -> out of bounds
        #  0 -> normal tile
        #  4 -> goal
        #  8 -> block
        self.base_env = np.ndarray([[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                                    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                                    [-1, -1,  0,  0,  0, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                                    [-1, -1,  0,  0,  0,  0,  0,  0, -1, -1, -1, -1, -1, -1],
                                    [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1, -1],
                                    [-1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
                                    [-1, -1, -1, -1, -1, -1, -1,  0,  0,  4,  0,  0, -1, -1],
                                    [-1, -1, -1, -1, -1, -1, -1, -1,  0,  0,  0, -1, -1, -1],
                                    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                                    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]])

        pass

    def _get_obs(self):
        return {"agent": self._agent_location, "target": self._target_location}

    def reset(self):
        # set both of the agent's coords to (4, 4) and (4, 4)
        self.block.set_coords(4, 4, 4, 4)

        # reset the environment (important to undo any obstacle interactions)
        self.current_env = self.base_env

        # place the agent in the environment using its position
        state = np.copy(self.current_env)
        state[4, 4] = 8
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
                self.block.moveLef()
            case 3:
                self.block.moveDown()

        # reward is -1 unless the agent hit the goal
        reward = -1

        # check if the agent is out of bounds -> reset to the start
        x1, y1, x2, y2 = self.block.get_coords()
        if (self.current_env[x1, y1] == -1 or self.current_env[x2, y2] == -1):
            self.block.set_coords(4, 4, 4, 4)

        # check if the agent is on a button -> change the current_env to reflect this

        # check if the agent is on the goal -> set done to True
        if(self.current_env[x1, y1] == 4 and self.current_env[x2, y2] == 4):


        # place the agent in the environment using its position

        # return state, reward,






