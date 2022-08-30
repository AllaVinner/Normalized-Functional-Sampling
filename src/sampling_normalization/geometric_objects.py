import numpy as np

def spiral(t, initial_angle=0, angular_freq=2*np.pi):
    x = t*np.cos(t*angular_freq+initial_angle)
    y = t*np.sin(t*angular_freq+initial_angle)
    return np.stack([x,y], axis=-1)   

    

