
import matplotlib.pyplot as plt
from cycler import cycler

plt.rcParams['axes.prop_cycle'] = cycler('color', ['lightblue', 'lightgreen', 'coral'])

line_params = {
    'color': 'gray',
    'linewidth': 2,
    'linestyle': '--',
}

scatter_params = {
    's': 50,
    'color': 'lightblue',
    'edgecolors': 'gray',
    'alpha': 0.8
}