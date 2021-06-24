# %% Setup
from sklearn.model_selection import learning_curve
from sklearn.datasets import make_blobs
from sklearn.ensemble import RandomForestClassifier as RandForClassy
import numpy as np
import mratplotlib.pyplot as plt
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
# plt.savefig('..\images\RAND_FOREST-CLASS-MODEL_200.jpg')
model = RandForClassy(n_estimators=500)
visualize_classifier(model, X, y, cmap='rainbow')
# plt.savefig('..\images\RNAD_FOREST-CLASS-MODEL_500.jpg')
# %% BEST MODEL


def plot_learning_curve(Esitmator, X, y, axes=None, cv=5, n_jobs=None, train_sizes=np.linspace(.1, 1.0, 5)):
    if axes is None:
        _, axes = plt.subplots(1, 3, figsize=(20, 5))

    axes[0].set_xlabel("Training examples")
    axes[0].set_ylabel("Score")

    train_sizes, train_scores, test_scores, fit_times, _ = \
        learning_curve(estimator, X, y, cv=cv, n_jobs=n_jobs,
                       train_sizes=train_sizes,
                       return_times=True)
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    fit_times_mean = np.mean(fit_times, axis=1)
    fit_times_std = np.std(fit_times, axis=1)

    # Plot learning curve
    axes[0].grid()
    axes[0].fill_between(train_sizes, train_scores_mean - train_scores_std,
                         train_scores_mean + train_scores_std, alpha=0.1,
                         color="r")
    axes[0].fill_between(train_sizes, test_scores_mean - test_scores_std,
                         test_scores_mean + test_scores_std, alpha=0.1,
                         color="g")
    axes[0].plot(train_sizes, train_scores_mean, 'o-', color="r",
                 label="Training score")
    axes[0].plot(train_sizes, test_scores_mean, 'o-', color="g",
                 label="Cross-validation score")
    axes[0].legend(loc="best")

    # Plot n_samples vs fit_times
    axes[1].grid()
    axes[1].plot(train_sizes, fit_times_mean, 'o-')
    axes[1].fill_between(train_sizes, fit_times_mean - fit_times_std,
                         fit_times_mean + fit_times_std, alpha=0.1)
    axes[1].set_xlabel("Training examples")
    axes[1].set_ylabel("fit_times")
    axes[1].set_title("Scalability of the model")

    # Plot fit_time vs score
    axes[2].grid()
    axes[2].plot(fit_times_mean, test_scores_mean, 'o-')
    axes[2].fill_between(fit_times_mean, test_scores_mean - test_scores_std,
                         test_scores_mean + test_scores_std, alpha=0.1)
    axes[2].set_xlabel("fit_times")
    axes[2].set_ylabel("Score")
    axes[2].set_title("Performance of the model")

    return plt


fig, axes = plt.subplots(3, 1, figsize=(10, 15))


# Cross validation with 100 iterations to get smoother mean test and train
# score curves, each time with 20% data randomly selected as a validation set.
axes[0].set_title('LEARNING CURVES')
estimator = RandForClassy()
plot_learning_curve(estimator, X, y, axes=axes,
                    cv=50, n_jobs=4)


plt.show()
# %%
