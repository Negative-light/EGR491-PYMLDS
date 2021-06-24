# %% Setup
from sklearn.datasets import make_blobs
from sklearn.ensemble import RandomForestClassifier as RandForClassy
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# %% Getting Data

X, y = make_blobs(500, 2, centers=10, cluster_std=1, random_state=1892)

plt.scatter(X[:, 0], X[:, 1], c=y, s=30, cmap='jet',
            clim=(y.min(), y.max()), zorder=3)
plt.axis('off')

plt.savefig('..\images\RAND_FOREST-CLASS-DATA.jpg')
# %% Helper Function From Text


def visualize_classifier(model, X, y, ax=None, cmap='rainbow'):
    ax = ax or plt.gca()  # Set the Plot axis

    # Plot the training points
    ax.scatter(X[:, 0], X[:, 1], c=y, s=30, cmap=cmap,
               clim=(y.min(), y.max()), zorder=3)  # Create a scatter plot of the data
    ax.axis('tight')  # Set the axis Range to tight
    ax.axis('off')  # Turn Off Axis Desplay
    xlim = ax.get_xlim()  # Get The X/Y LIMITS
    ylim = ax.get_ylim()

    # fit the estimator
    model.fit(X, y)  # Fit the model
    xx, yy = np.meshgrid(np.linspace(*xlim, num=200),
                         np.linspace(*ylim, num=200))  # Make grid of datapoints
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(
        xx.shape)  # Use model to predict data

    # Create a color plot with the results
    n_classes = len(np.unique(y))
    contours = ax.contourf(xx, yy, Z, alpha=0.3,
                           levels=np.arange(n_classes + 1) - 0.5,
                           cmap=cmap, clim=(y.min(), y.max()),
                           zorder=1)

    ax.set(xlim=xlim, ylim=ylim)


# %% Setting UP and Running Module

model = RandForClassy(n_estimators=200)
visualize_classifier(model, X, y, cmap='seismic')
plt.savefig('..\images\RAND_FOREST-CLASS-MODEL_200.jpg')
model = RandForClassy(n_estimators=500)
visualize_classifier(model, X, y, cmap='rainbow')
plt.savefig('..\images\RNAD_FOREST-CLASS-MODEL_500.jpg')
# %%
