# %% HEADER

import pandas as pd
import seaborn as sns
from sklearn import gaussian_process
from scipy.stats import gaussian_kde
import matplotlib.pyplot as plt
import numpy as np
# %% LINE PLOT

plt.style.use('seaborn-whitegrid')

fig = plt.figure()
ax = plt.axes()
x = np.linspace(-10, 10, 100)
ax.plot(x, 10*np.sin(x))
plt.plot(x, np.absolute(x), '--')
plt.savefig('../images/line.jpg')
# %% SCATTER PLOT

x = np.linspace(-10, 10, 100)
y = np.random.random_integers(-10, 10, (100))
plt.plot(x, y)

r = 100*np.random.random(100)
clr = np.random.random(100)
plt.scatter(x, y, s=r, c=clr, cmap='viridis')
plt.savefig('../images/scatter.jpg')

# %% Contour Plots


def func(x, y):
    return ((np.sin(x)**2) + (np.cos(y)**2)) - np.cos(np.linspace(0, 20, 100))


x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)
x, y = np.meshgrid(x, y)
z = func(x, y)
fig, ax = plt.subplots(1, 3, sharex='col', sharey='row')
ax[0].contour(x, y, z, 20, cmap='brg')
ax[1].contourf(x, y, z, 20, cmap='brg')
ax[2].imshow(z, extent=[0, 10, 0, 10], origin='lower', cmap='brg')
plt.show()
plt.savefig('../images/contour.jpg')
# %% Density Plots


# %% Histograms
data = np.random.randn(100)
fig = plt.figure()
fig, ax = plt.subplots(1, 3, sharex='col')

ax[0].hist(data)
ax[1].hist(data, bins=5)
ax[2].hist(data, bins=20, histtype='stepfilled', edgecolor='steelblue')
plt.savefig('..\images\graph_hist.jpg')
# %% Bins
data_x = np.random.randint(0, 10, 10000)
data_y = np.random.randint(0, 10, 10000)
a = 0.5
plt.hist2d(data_x, data_y, cmap='RdBu', bins=2, alpha=a)
plt.hist2d(data_x, data_y, cmap='RdGy', bins=4, alpha=a)
plt.hist2d(data_x, data_y, cmap='RdBu_r', bins=8, alpha=a/2)
plt.hist2d(data_x, data_y, cmap='RdGy_r', bins=16, alpha=a/2)
plt.savefig('..\images\graph_hist2d.jpg')
# %% Hex Bins
data_x = np.random.randn(10000)
data_y = np.random.randn(10000)*2
data_x = np.sin(data_x)
data_y = np.cos(data_y)
fig, ax = plt.subplots(5, 5, sharex='col', sharey='row', figsize=(25, 25))
for i in range(2, 7):
    for b in range(2, 7):
        ax[i-2, b-2].set_title(str(i) + ':' + str(b))
        ax[i-2, b-2].hexbin(data_x, data_y, cmap='Reds',
                            gridsize=[i, i+1], bins=b)
plt.savefig('../images/hexbins2.jpg')
# %% KDE
data_x = np.random.randn(10000)
data_y = np.random.randn(10000)*2
data_x = np.sin(data_x*np.pi)
data_y = np.cos(data_y*np.pi)
data = np.vstack([data_x, data_y])
kde = gaussian_kde(data)

xgrid = np.linspace(-1, 1, 100)
ygrid = np.linspace(-1, 1, 100)
Xgrid, Ygrid = np.meshgrid(xgrid, ygrid)
Z = kde.evaluate(np.vstack([Xgrid.ravel(), Ygrid.ravel()]))
plt.imshow(Z.reshape(Xgrid.shape),
           origin='lower', aspect='auto',
           extent=[-1, 1, -1, 1],
           cmap='coolwarm')
plt.savefig('../images/KDE.jpg')

# %% ERROR BAR

x = np.linspace(-10, 10, (5))
y = np.random.randint(-10, 10, (5))
x += np.sin(y)
# plt.plot(x, y, linestyle=':')

###########################
# Basic Error Bar
plt.errorbar(x, y, xerr=0.8, yerr=0.8, ecolor='purple',
             fmt='.k', color='blue', capsize=3)
plt.savefig('../images/basicErr.jpg')  # saving the plot as an image

##########################
# Continyous Error
plt.fill_between(x, y+0.8, y-0.8, color='red', alpha=0.5,
                 where=[True, True, False, True, True], interpolate=True)
plt.savefig('../images/contErr.jpg')
#####

# %% Cross Bar

data_x = np.random.randint(0, 10, 10000)
data_y = np.random.randint(0, 10, 10000)
a = 0.5
color_map = plt.cm.get_cmap('RdBu', 5)
plt.hist2d(data_x, data_y, cmap=color_map, bins=16, alpha=a)
plt.hist2d(data_x, data_y, cmap=color_map, bins=8, alpha=a)
plt.hist2d(data_x, data_y, cmap=color_map, bins=4, alpha=a)
plt.hist2d(data_x, data_y, cmap=color_map, bins=2, alpha=a)
plt.colorbar(ticks=range(5), label='5 colors :)')
plt.clim(-0.5, 0.5)
plt.savefig('../images/clrbar.jpg')


# %% Trans Axis

fig, ax = plt.subplots(facecolor='yellow')
ax.axis([-1, 1, -1, 1])
ax.text(0, 0, '.  Origin')
ax.text(0, 0, '. Bottom Corner', transform=ax.transAxes)
ax.text(0.5, 0.5, 'Origin 2 .',  transform=fig.transFigure, ha='right')

plt.savefig('../images/text.jpg')
ax.axis([-2, 2, -1, 2])
ax.annotate('NOTICE \n That Origin did not move',
            xy=(0, 0), xytext=(1, 1),
            arrowprops=dict(facecolor='black', shrink=1.5))
plt.savefig('../images/text2.jpg')
fig

# %% 3D Plots
ax = plt.axes(projection='3d')
x = np.linspace(0, 100, 100)
y = np.sin(x)
z = np.sin(2*x) - np.arcsin(y)

ax.plot3D(x, y, z, 'Blue')
y *= 2
ax.scatter3D(x, y, z, c=y, cmap='binary')
plt.savefig('../images/3d-plt.jpg')

# %% 3d Contour


def f(x, z):
    return np.sin(x)**2 + np.cos(z)**2


x = np.linspace(-10, 10, 100)
z = np.linspace(-10, 10, 100)

X, Z = np.meshgrid(x, y)
Y = f(X, Z)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 100, cmap='plasma')
plt.savefig('../images/contour3d.png')
# %% Seaborn
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)

sns.set()  # Activates seaborn
plt.plot(x, y)
plt.savefig('..\images\sns-plt.jpg')
plt.clf()  # Clears the figure
plt.cla()  # Clears the Axis
# HISTOGRAMS
data = np.random.randint(0, 10, (1000, 2))
data = pd.DataFrame(data, columns=['x', 'y'])

for col in 'xy':
    plt.hist(data[col], alpha=0.5)

plt.savefig('..\images\sns-hist.jpg')
# Smooth HIstograms
plt.clf()
plt.cla()
for col in 'xy':
    sns.kdeplot(data[col], shade=True)

plt.savefig('..\images\sns-hist-kde.jpg')

# DIstplots
plt.clf()
plt.cla()
sns.displot(data['x'])
sns.distplot(data['y'])

plt.savefig('..\images\sns-dist-kde.jpg')

# KDE Plots
plt.clf()
plt.cla()
sns.kdeplot(data['x'], data['y'])
plt.savefig('..\images\sns-kde.jpg')
sns.jointplot("x", "y", data, kind='kde')
plt.savefig('..\images\sns-join-kde.jpg')
sns.jointplot("x", "y", data, kind='hex')
plt.savefig('..\images\sns-join-hex.jpg')

# Pair plots
plt.clf()
plt.cla()
sns.pairplot(sns.load_dataset('iris'), hue='species', size=1)
plt.savefig('..\images\sns-pair.jpg')
# %% GridSpc

# Create some normally distributed data

x = np.random.randint(-10, 10, 1000)
y = np.random.randint(-10, 10, 1000)
y += x
# Set up the axes with gridspec
fig = plt.figure(figsize=(6, 6))
grid = plt.GridSpec(4, 4, hspace=0.2, wspace=0.2)
main_ax = fig.add_subplot(grid[:-1, 1:])
y_hist = fig.add_subplot(grid[:-1, 0], xticklabels=[], sharey=main_ax)
x_hist = fig.add_subplot(grid[-1, 1:], yticklabels=[], sharex=main_ax)

# scatter points on the main axes
main_ax.plot(x, y, 'ob', markersize=3, alpha=0.2)

# histogram on the attached axes
x_hist.hist(x, 40, histtype='stepfilled',
            orientation='vertical', color='Blue')
x_hist.invert_yaxis()

y_hist.hist(y, 40, histtype='stepfilled',
            orientation='horizontal', color='Orange')
y_hist.invert_xaxis()
plt.savefig('..\images\gridSpec.jpg')
# %% DO NOT INCLUDE IN EXAMPLES=
plt.show()

# %%
