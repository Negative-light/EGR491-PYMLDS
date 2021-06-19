import itertools

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def data_gen():
    for cnt in itertools.count():
        t = cnt / 10
        yield t, np.random.rand(5).sum()


def init():
    ax.set_ylim(-2.1, 5.1)
    ax.set_xlim(0, 10)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,


xdata = []
ydata = []
fig, ax = plt.subplots()
line, = ax.hist2d(xdata, ydata, bins=10)
ax.grid()
xdata, ydata = [], []


def run(data):
    # update the data
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()

    if t >= xmax:
        ax.set_xlim(xmin, 2*xmax)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)

    return line,


ani = animation.FuncAnimation(fig, run, data_gen, interval=10, init_func=init)
plt.show()
