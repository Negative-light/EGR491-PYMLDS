# %% IMPORTS
from skimage.io import imread
from itertools import chain

import matplotlib.pyplot as plt
import numpy as np
import skimage.data
from skimage import color, data, feature, transform
import sklearn
from sklearn.datasets import fetch_lfw_people
from sklearn.ensemble import RandomForestClassifier as RandForClassy
from sklearn.feature_extraction.image import PatchExtractor
from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import LinearSVC

# %% GET FALSE DATA
imgs_to_use = ['camera', 'text', 'coins', 'moon',
               'page', 'clock', 'immunohistochemistry',
               'chelsea', 'coffee', 'hubble_deep_field']
images = [color.rgb2gray(getattr(data, name)())
          for name in imgs_to_use]
# %% GET TRUE
faces = fetch_lfw_people()
positive_patches = faces.images
# %% FUNCTION DEFINITIONS


def extract_patches(img, N, scale=1.0, patch_size=positive_patches[0].shape):
    extracted_patch_size = tuple((scale * np.array(patch_size)).astype(int))
    extractor = PatchExtractor(patch_size=extracted_patch_size,
                               max_patches=N, random_state=0)
    patches = extractor.transform(img[np.newaxis])
    if scale != 1:
        patches = np.array([transform.resize(patch, patch_size)
                            for patch in patches])
    return patches


def sliding_window(img, patch_size=positive_patches[0].shape,
                   istep=2, jstep=2, scale=1.0):
    Ni, Nj = (int(scale * s) for s in patch_size)
    for i in range(0, img.shape[0] - Ni, istep):
        for j in range(0, img.shape[1] - Ni, jstep):
            patch = img[i:i + Ni, j:j + Nj]
            if scale != 1:
                patch = transform.resize(patch, patch_size)
            yield (i, j), patch


negative_patches = np.vstack([extract_patches(im, 1000, scale)
                              for im in images for scale in [0.5, 1.0, 2.0]])

# %% EXTRACT HOG FEATURES
X_train = np.array([feature.hog(im)
                    for im in chain(positive_patches,
                                    negative_patches)])
y_train = np.zeros(X_train.shape[0])
y_train[:positive_patches.shape[0]] = 1

# %%
grid = GridSearchCV(LinearSVC(max_iter=100000), {'C': [1.0, 2.0, 4.0, 8.0]})
grid.fit(X_train, y_train)

model = grid.best_estimator_
model.fit(X_train, y_train)
# %% RUN FIMPLE TEST IMAGE


def prepImg(img):

    test_image = img
    test_image = skimage.color.rgb2gray(test_image)
    test_image = skimage.transform.rescale(test_image, 0.5)
    test_image = test_image[:160, 40:180]

    return test_image
# %% PLOT TEST IMAGE


def pltImg(img):
    img = prepImg(img)
    indices, patches = zip(*sliding_window(img))
    patches_hog = np.array([feature.hog(patch) for patch in patches])
    patches_hog.shape

    labels = model.predict(patches_hog)
    labels.sum()

    fig, ax = plt.subplots()
    ax.imshow(img, cmap='gray')
    ax.axis('off')

    Ni, Nj = positive_patches[0].shape
    indices = np.array(indices)
    valid_indicies = indices[labels == 1]
    for i, j in valid_indicies:
        ax.add_patch(plt.Rectangle((j, i), Nj, Ni, edgecolor='red',
                                   alpha=0.2, lw=2, facecolor='none'))
    mean_j = np.mean(valid_indicies, axis=1)
    mean_i = np.mean(valid_indicies, axis=0)

    print(mean_i)

    return plt


pltImg(skimage.data.astronaut())

# %%
exit = False

while(not exit):
    file = input('Enter a File Path:')
    print('Prepring Display')
    pltImg(imread(file))
    plt.show()
    if(input('Woud you like to coninue [Y/n]') == 'n'):

        print('Goodbye')
        exit = True

# %%
