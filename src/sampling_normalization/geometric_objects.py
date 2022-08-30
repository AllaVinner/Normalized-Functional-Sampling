import numpy as np


from abc import ABC, abstractmethod

class Geometric(ABC):

    @abstractmethod
    def __call__(self, t, *args, **kwargs):
        pass


class Spiral(Geometric):

    def __init__(self, initial_angle:float=0., angular_frequency:float=2*np.pi):
        self.initial_angle = initial_angle
        self.angular_frequency = angular_frequency

    def __call__(self, t, *args, **kwargs):
        angle = self.angular_freq + self.initial_angle
        x = t*np.cos(t*angle)
        y = t*np.sin(t*angle)
        return np.stack([x,y], axis=-1)   

    

