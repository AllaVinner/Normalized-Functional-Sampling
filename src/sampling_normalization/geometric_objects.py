from typing import List

import numpy as np
from sampling_normalization.

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

    def __init__(self, initial_angle:float=0., angular_frequency:float=2*np.pi, t_max:float=2*np.pi, *args, **kwargs):
        self.initial_angle = initial_angle
        self.angular_frequency = angular_frequency
        self.t_max = t_max
        self.length = self.length_at(self.t_max)
        self.domain = [0, self.t_max]

    def __call__(self, t, *args, **kwargs):
        is_in_domain = self.in_domain(t)
        if isinstance(is_in_domain, bool):
            assert is_in_domain
        else:
            assert is_in_domain.all()
        x = t*np.cos(t*self.angular_frequency + self.initial_angle)
        y = t*np.sin(t*self.angular_frequency + self.initial_angle)
        return np.stack([x,y], axis=-1)

    def in_domain(self, t):
        return self.domain[0] <= t <= self.domain[1]


    def inv_length(self, l: float) -> float:
        return inv_value(self.length, target_value = l, min_guess=0, max_guess = self.t_max)

    def sample(self, num_samples):
        t = self.t_max*np.random.random(num_samples)
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