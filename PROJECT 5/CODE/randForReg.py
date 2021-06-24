### CEW EXAMPLE ###
# %% Setup
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.signal import sawtooth
from sklearn.datasets import make_blobs
from sklearn.ensemble import RandomForestRegressor as RandForRegy

sns.set()
rng = np.random.RandomState(420)
x = np.linspace(0, 12, 200)
# SIGNAL FUNCTION


def signal(x, noise_mult=1):
    base = np.sin(2*np.pi*x)
    saw = sawtooth(3*np.pi*x)
    noise_a = 0.5 * (np.random.randint(-90, 90, len(x))/100)
    noise_b = 0.2 * np.random.randint(0, 1) * np.cos(3*sawtooth(x)+base)
    noise = (noise_a + noise_b)
    return base + saw + noise*noise_mult


y = signal(x)


# %% SETTING UP/RUNNING OUT MODEL
model_200 = RandForRegy(200)
model_500 = RandForRegy(500)

model_200.fit(x[:, None], y)
model_500.fit(x[:, None], y)

y_fit_200 = model_200.predict(x[:, None])
y_fit_500 = model_500.predict(x[:, None])
# %% FILL OUT

plt.plot(x, y_fit_200, '--', linewidth=2)
plt.plot(x, y_fit_500, '-.', linewidth=2)
plt.plot(x, signal(x, noise_mult=0), alpha=0.4, c='red')
plt.errorbar(x, y, 0.5, fmt='o', alpha=0.1)
plt.legend()
plt.savefig('..\images\RAND_FOREST-REG-ALL.png')
# %%
