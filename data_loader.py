import numpy as np
from fitting_and_analysis import CurveFitFuncs
cff = CurveFitFuncs()

class DataLoader():
    def __init__(self, filename):
        directory = 'pendulum_data/%s.txt' % filename
        # directory = filename
        file = open(directory, 'r')
        raw_data = file.read()
        raw_data = raw_data.split('\n')[2:500]
        raw_data = [row.split('\t') for row in raw_data]
        raw_data = [['0' if entry == '' else entry for entry in row] for row in raw_data]
        raw_data = [[float(entry) for entry in row] for row in raw_data]
        self.full_data = np.zeros((len(raw_data), len(raw_data[0])), dtype=float)

        for i in range(len(self.full_data)):
            self.full_data[i] += np.array(raw_data[i])

        self.full_data = self.full_data.T
        
        raw_times = self.full_data[0]
        raw_positions = self.full_data[1]
        
        self.zeroed_times = cff.remove_systematic_error(raw_times)
        self.zeroed_positions = cff.remove_systematic_error(raw_positions)
        
        self.y = self.zeroed_positions
        self.y_error = np.zeros_like(self.zeroed_positions) + 4
        
        self.x = self.zeroed_times
        self.x_error = np.zeros_like(self.zeroed_times) + 0.0005
