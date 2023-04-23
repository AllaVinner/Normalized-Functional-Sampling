import numpy as np
from scripts.utils import inv_value


class Spiral():

    def __init__(self, initial_angle:float=0., angular_frequency:float=2*np.pi, t_max:float=2*np.pi, *args, **kwargs):
        self.initial_angle = initial_angle
        self.angular_frequency = angular_frequency
        self.t_max = t_max
        self.length = self.length_at(self.t_max)
        self.domain = [0, self.t_max]

    def __call__(self, t, *args, **kwargs):
        x = t*np.cos(t*self.angular_frequency + self.initial_angle)
        y = t*np.sin(t*self.angular_frequency + self.initial_angle)
        return np.stack([x,y], axis=-1)

    def in_domain(self, t):
        return self.domain[0] <= t <= self.domain[1]

    def length_at(self, t):
        return 1/2*t*(np.sqrt(1+t*t))+1/2*np.log(t+np.sqrt(1+t*t))

    def inv_length(self, l: float) -> float:
        return inv_value(self.length_at, target_value=l, min_guess=0, max_guess=self.t_max)

    def sample(self, num_samples):
        t = self.t_max*np.random.random(num_samples)
        return self(t)


class NormalizedSpiral():

    def __init__(self, initial_angle:float=0., angular_frequency:float=2*np.pi, t_max:float=2*np.pi, *args, **kwargs):
        self.initial_angle = initial_angle
        self.angular_frequency = angular_frequency
        self.t_max = t_max
        self.length = self.length_at(self.t_max)
        self.domain = [0, self.t_max]

    def __call__(self, t, *args, **kwargs):
        t = inv_value(self.length_at, target_value=self.length*t/self.t_max,
                     min_guess=0, max_guess=self.t_max)
        x = t*np.cos(t*self.angular_frequency + self.initial_angle)
        y = t*np.sin(t*self.angular_frequency + self.initial_angle)
        return np.stack([x,y], axis=-1)

    def in_domain(self, t):
        return self.domain[0] <= t <= self.domain[1]

    def length_at(self, t):
        return 1/2*t*(np.sqrt(1+t*t))+1/2*np.log(t+np.sqrt(1+t*t))


class Disk():

    def __init__(self, radius: float, *args, **kwargs):
        self.radius = radius
        self.length = self.area_at_radius(self.radius)
        self.domain = [[0, self.radius], [0, np.pi*2]]

    def __call__(self, r, alpha, *args, **kwargs):
        x = r*np.cos(alpha)
        y = r*np.sin(alpha)
        return np.stack([x,y], axis=-1)

    def in_domain(self, t):
        return self.domain[0] <= t <= self.domain[1]

    def area_at_radius(self, r):
        return r*r*np.pi

    def inv_area(self, area: float) -> float:
        return np.sqrt(area/np.pi)



