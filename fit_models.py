import numpy as np
import fitted_models

class Gaussian(): # height is usually 1; not probability density
    def __init__(self):
        self.number_of_parameters = 4
        self.CorrespondingFittedFunction = fitted_models.Gaussian

    def __call__(self, x, base, scale, mu, sigma):
        result = base + scale * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
        return result

class GaussianZeroCenter(): # height is usually 1; not probability density
    def __init__(self):
        self.number_of_parameters = 3
        self.CorrespondingFittedFunction = fitted_models.GaussianZeroCenter

    def __call__(self, x, base, scale, sigma):
        result = base + scale * np.exp(-0.5 * ((x) / sigma) ** 2)
        return result

class Linear():
    def __init__(self):
        self.number_of_parameters = 2
        self.CorrespondingFittedFunction = fitted_models.Linear

    def __call__(self, x, m, c):
        result = m*x + c
        return result
    
class DecayingSinusoid():
    def __init__(self):
        self.number_of_parameters = 5
        self.CorrespondingFittedFunction = fitted_models.DecayingSinusoid
        
    def __call__(self, t, base, amplitude, period, phase, decay_constant):
        result = base + np.exp(-t / decay_constant) * amplitude * np.cos((2*np.pi / period) * t + phase)
        return result