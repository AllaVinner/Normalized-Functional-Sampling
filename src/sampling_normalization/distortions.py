from abc import ABC, abstractmethod
from dis import dis


class Distortion(ABC):

    def __call__(self, *args, **kwargs):
        pass


class ConstantRadialDistortion(Distortion):

    def __init__(self, distortion_scale:float, distortion_shape):
        self.distortion_scale = distortion_scale
        self.distortion_shape = distortion_shape
        self.distortion_dim = len(distortion_shape)
    

    def __call__(self, samples, *args, **kwargs):
        samples_shape = samples.shape[-self.distortion_dim:]
        assert all([samples_shape[i] == self.distortion_shape[i] for i in range(self.distortion_dim)]), 'samples have non compatible shape'
        return super().__call__(*args, **kwargs)









