import numpy as np

import data_loader
import fit_models
import fitting

class Calibration():
    def __init__(self):
        filename = 'vary_angle_20deg'
        directory = 'pendulum_data/%s.txt' % filename
        file = open(directory, 'r')
        raw_data = file.read()
        raw_data = raw_data.split('\n')[2:1000]
        raw_data = [row.split('\t') for row in raw_data]
        raw_data = [['0' if entry == '' else entry for entry in row] for row in raw_data]
        raw_data = [[float(entry) for entry in row] for row in raw_data]
        full_data = np.zeros((len(raw_data), len(raw_data[0])), dtype=float)

        for i in range(len(full_data)):
            full_data[i] += np.array(raw_data[i])

        full_data = full_data.T


        raw_positions = full_data[1]


        filename = 'calibration_data_vary_angle_20deg'
        directory = 'pendulum_data/%s.txt' % filename
        file = open(directory, 'r')
        calibrated_data = file.read()
        calibrated_data = calibrated_data.split('\n')[2:-1]
        calibrated_data = [row.split('\t') for row in calibrated_data]
        calibrated_data = [['0' if entry == '' else entry for entry in row] for row in calibrated_data]
        calibrated_data = [[float(entry) for entry in row] for row in calibrated_data]
        full_data = np.zeros((len(calibrated_data), len(calibrated_data[0])), dtype=float)

        for i in range(len(full_data)):
            full_data[i] += np.array(calibrated_data[i])

        full_data = full_data.T


        calibrated_positions = full_data[1]

        raw_positions_mean = np.mean(raw_positions)
        calibrated_positions_mean = np.mean(calibrated_positions)


        self.calibration_factor = calibrated_positions_mean / raw_positions_mean

    def calibrate(self, x):
        x = x * self.calibration_factor
        return x