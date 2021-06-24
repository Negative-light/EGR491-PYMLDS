# %% SKIMAGE_TEST
import os
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import skimage.data
from skimage import color, data, feature

sns.set()


image = color.rgb2gray(data.brick())
plt.axis('off')
plt.imshow(image, cmap='gray')
plt.title('YOU HAVE HIT A BRICK WALL')
