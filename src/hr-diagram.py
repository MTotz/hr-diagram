import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib import cm
import seaborn as sns


class MidpointNormalize(colors.Normalize):
    """
    Normalise the colorbar so that diverging bars work there way either side from a prescribed midpoint value)
    Function taken from http://chris35wills.github.io/matplotlib_diverging_colorbar/

    e.g. im=ax1.imshow(array, norm=MidpointNormalize(
        midpoint=0.,vmin=-100, vmax=100))
    """

    def __init__(self, vmin=None, vmax=None, midpoint=None, clip=False):
        self.midpoint = midpoint
        colors.Normalize.__init__(self, vmin, vmax, clip)

    def __call__(self, value, clip=None):
        # I'm ignoring masked values and all kinds of edge cases to make a
        # simple example...
        x, y = [self.vmin, self.midpoint, self.vmax], [0, 0.5, 1]
        return np.ma.masked_array(np.interp(value, x, y), np.isnan(value))


df = pd.read_csv('../database/hygdata_v3.csv',
                 usecols=['absmag', 'spect', 'lum', 'ci'])

fig, ax = plt.subplots()
ax.set_facecolor('black')
palette = cm.get_cmap("RdYlBu", 12)
plt.scatter(x="ci", y="lum", data=df.iloc[::15], norm=MidpointNormalize(midpoint=0, vmin=-0.33, vmax=1.4),
            edgecolor=None, alpha=1, s=5, c="ci", cmap="RdYlBu_r")
ax.set(yscale="log")
ax.set_xlim(-0.5, 2.3)
plt.title("Hertzsprung-Russell Diagram")
ax.set_xlabel("Color Index")
ax.set_ylabel("Luminosity")
plt.show()
