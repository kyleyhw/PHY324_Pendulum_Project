import matplotlib.pyplot as plt
from matplotlib import rc

font = {'family': 'DejaVu Sans',
        'weight': 'normal',
        'size': 22}
rc('font', **font)
import numpy as np

import data_loader
import fit_models
import fitting


def run_main(filename, show=False, save=False):
    data = data_loader.DataLoader(filename)
    model = fit_models.DecayingSinusoid()

    try:
        fit = fitting.Fitting(model=model, x=data.x, x_error=data.x_error, y_measured=data.y, y_error=data.y_error,
                              units_for_parameters=('', '', '', '', ''), p0=(150, 100, 1, 1, 0.02))
    except RuntimeError:
        fit = fitting.Fitting(model=model, x=data.x, x_error=data.x_error, y_measured=data.y, y_error=data.y_error,
                              units_for_parameters=('', '', '', '', ''), p0=(150, 100, 1, -1, 0.02))

    fig, ax = plt.subplots(1, 1, figsize=(16, 9))

    fit.scatter_plot_data_and_fit(ax)

    ax.set_title('')
    ax.grid(visible=True, which='both')
    ax.set_ylabel('')
    ax.set_xlabel('')

    if save:
        fig.savefig('fits/' + filename + '.png')
    if show:
        fig.show()

def single_run_main(filename):
    run_main(filename, show=True, save=True)

def run_main_from_dict(filenames):
    for filename in filenames.values():
        print(filename)
        run_main(filename, show=False, save=True)


vary_angle_filenames = {angle : 'vary_angle_%s' % angle for angle in ['20deg', '40deg', '60deg', '80deg']}
vary_l_filenames = {l : 'vary_l_%s' % l for l in ['15cm', '20cm', '25cm', '30cm', '35cm']}
vary_m_filenames = {m : 'vary_m_%s' % m for m in ['50g', '100g', '150g', '200g']}


all_filenames = {**vary_angle_filenames, **vary_l_filenames, **vary_m_filenames}


# filename = all_filenames['20deg']
# single_run_main(filename)

run_main_from_dict(all_filenames)