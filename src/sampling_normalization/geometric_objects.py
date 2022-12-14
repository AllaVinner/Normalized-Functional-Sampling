import numpy as np


from abc import ABC, abstractmethod

class Geometric(ABC):

    @property
    @abstractmethod
    def dimension(self)->int:
        pass

    @property
    @abstractmethod
    def enclosing_dimension(self)->int:
        pass

    @abstractmethod
    def __call__(self, t, *args, **kwargs):
        pass


class Spiral(Geometric):

    def __init__(self, initial_angle:float=0., angular_frequency:float=2*np.pi):
        self.initial_angle = initial_angle
        self.angular_frequency = angular_frequency

    def __call__(self, t, *args, **kwargs):
        x = t*np.cos(t*self.angular_frequency + self.initial_angle)
        y = t*np.sin(t*self.angular_frequency + self.initial_angle)
        return np.stack([x,y], axis=-1)   

    @property
    def dimension(self) -> int:
        return 1
    
    @property
    def enclosing_dimension(self) -> int:
        return 2
    

