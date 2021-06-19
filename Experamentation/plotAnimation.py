# %% Imports

from matplotlib import rc
from IPython.display import HTML
from matplotlib import animation
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mtp


# %%

fig = plt.figure()
ax = plt.subplot(1, 2, 1)
line, = ax.plot([], [])


def frame(n):
    x = np.linspace(0, 100, 1000)
    y = np.sin(x + n)
    line.set_data(x, y)
    return (line,)


anim = animation.FuncAnimation(fig, frame, frames=1000, interval=10, blit=True)
plt.show()


# %%
