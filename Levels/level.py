from abc import ABC, abstractmethod
import gym

class Level(gym.env,ABC):

    @abstractmethod
    def step(self):
        raise NotImplementedError

    def reset