import numpy as np
from sampling_normalization.algoritms import inv_value

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

    def __init__(self, initial_angle:float=0., angular_frequency:float=2*np.pi, max_t:float=2*np.pi, *args, **kwargs):
        self.initial_angle = initial_angle
        self.angular_frequency = angular_frequency
        self.max_t = max_t

    def __call__(self, t, *args, **kwargs):
        assert t <= self.max_t
        x = t*np.cos(t*self.angular_frequency + self.initial_angle)
        y = t*np.sin(t*self.angular_frequency + self.initial_angle)
        return np.stack([x,y], axis=-1)   

    def length(self, t):
        return 1/2*t*np.sqrt(1+t*t)+1/2*np.log(t+np.sqrt(1+t*t))

    def inv_length(self, l):
        return inv_value(self.length, target_value = l, min_guess=0, max_guess = self.max_t)

    def sample(self, num_samples):
        t = self.max_t*np.random.random(num_samples)
        return self(t)


    @property
    def dimension(self) -> int:
        return 1
    
    @property
    def enclosing_dimension(self) -> int:
        return 2
    

class Disk(Geometric):
    def __init__(self):

    def __call__(self, r, alpha, *args, **kwargs):
        x = r*np.cos(alpha)
        y = r*np.sin(alpha)
        return np.stack([x,y], axis=-1)

    @property
    def dimension(self) -> int:
        return 2

    @property
    def enclosing_dimension(self) -> int:
        return 2