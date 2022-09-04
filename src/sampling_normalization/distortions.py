import numpy as np
from sklearn.preprocessing import normalize


def constant_radial_distortion(samples, distortion_std:float=0.01):
    unit_samples = normalize(samples)
    distortions = np.random.normal(scale=distortion_std, size=len(samples))
    return samples+np.diag(distortions)@unit_samples


def radial_distortion(samples, distortion_std:float=0.01):
    distortions = np.random.gamma(1/distortion_std**2, distortion_std**2, len(samples))
    print('Distortions: ', distortions)
    distortions = np.random.normal(scale=distortion_std, size=len(samples))
    return np.diag(distortions)@samples








