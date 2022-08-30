import numpy as np
from sampling_normalization import geometric_objects as go

class Sampler():

    def __init__(self, geometric: go.Geometric, limits = None, sampling_normalizer=None):
        self.dimension = geometric.dimension
        self.enclosing_dimension = geometric.enclosing_dimension
        self.geometric = geometric
    
    def __call__(self, size=(1,), squeeze_geometric_dimension:bool=True):
        if isinstance(size, int):
            size = (size,)
        if self.dimension > 1 or not squeeze_geometric_dimension:
            size = (*size, self.dimension)
        unit_samples = np.random.uniform(size=size)
        return self.geometric(unit_samples) 






