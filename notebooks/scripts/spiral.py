from typing import Callable

import numpy as np


class Spiral():

    def __init__(self, 
                 initial_angle:float=0., 
                 angular_frequency:float=2*np.pi, 
                 t_max:float=2*np.pi, 
                 *args, **kwargs):
        self.initial_angle = initial_angle
        self.angular_frequency = angular_frequency
        self.t_max = t_max
        self.length = self.length_at(self.t_max)
        self.domain = [0, self.t_max]

    def __call__(self, t, *args, **kwargs):
        x = t*np.cos(t*self.angular_frequency + self.initial_angle)
        y = t*np.sin(t*self.angular_frequency + self.initial_angle)
        return np.stack([x,y], axis=-1)

    def sample_normalized(self, num_samples):
        samples = self.t_max*np.random.random(num_samples)
        altered_samples = self.alter_samples(samples)
        return self(altered_samples)

    def alter_sample(self, samples):
        spiral_length = self.length_at_position(self.t_max)
        alterd_samples = self.position_at_length(spiral_length/self.t_max*alterd_samples)
        return alterd_samples

    def length_at_position(self, t):
        a = self.angular_frequency
        return 1/2*t*(np.sqrt(1+(a*t)**2))+1/(2*a)*np.log(a*t+np.sqrt(1+(a*t)**2))

    def position_at_length(self, l: float) -> float:
        return self._inv_value(self.length_at, target_value=l, min_guess=0, max_guess=self.t_max)


    def _inv_value(f: Callable, target_value: float, min_guess: float, max_guess: float, num_guesses: int = 50) -> float:
        x_guess = (max_guess + min_guess)/2
        for _ in range(num_guesses):
            guess_value = f(x_guess)
            if guess_value < target_value:
                min_guess = x_guess
                x_guess = (max_guess + x_guess)/2
            else:
                max_guess = x_guess
                x_guess = (min_guess + x_guess)/2

        return x_guess









