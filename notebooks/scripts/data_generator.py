
from scripts import geometrical_objects as go
import numpy as np

def generate_spiral_dataset(num_classes, num_samples_per_class, spiral_frequency, spiral_angular_lenght):
    spirals= [go.Spiral(initial_angle=2*np.pi-num_classes*i, angular_frequency=spiral_frequency, t_max=spiral_angular_lenght) for i in range(num_classes)]

    







