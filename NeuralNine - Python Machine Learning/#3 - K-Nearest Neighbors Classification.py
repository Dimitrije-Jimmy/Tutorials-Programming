# K-Nearest Neighbours Classification

# in depth blog post
# https://www.neuralnine.com/k-nearest-neighbors-classification-from-scratch-in-python/

# allows us to classify unknown data by looking at data that is already classified
#  - supervised learning

"""
The weight to height graph explained in '#1 - machine learning.txt'
We have classified data points, red and blue points
 we add a grey point and ask our model to decide wether it's a red point or blue
 it takes K amount of nearest neighbours to compare to
 it calculates how many points of which sector are nearest and thus puts it there
 if the nearest neighbours are 5 blue and 3 red, then it's a blue point
The amount of classes (groups) shouldn't be divisible by the number K
 if you have 3 classes don't pick K=3, because it would be indeterminate
If you say K=1 it fucks up because of outliers
"""

# We're going to be classifying the breast-cancer dataset from scikit-learn
#  this dataset has a lot of paramaters about cancer/different tumors,
#  and classifies wether the cancer is malignant or benign (bad or good)

from sklearn.datasets import load_breast_cancer         # for the dataset
from sklearn.neighbors import KNeighborsClassifier      # for the model
from sklearn.model_selection import train_test_split    # for splitting train and test data
import numpy as np

# First we look at the data
data = load_breast_cancer()
print(data)
print("_"*20)
print(data.feature_names)
print(data.target_names) # ['malignant' 'benign']
# 212 - Malignant, 357 - Benign


# tumor features:
# all the things we can use to classify whether the tumor is malignant or benign
"""
['mean radius' 'mean texture' 'mean perimeter' 'mean area'
 'mean smoothness' 'mean compactness' 'mean concavity'
 'mean concave points' 'mean symmetry' 'mean fractal dimension'
 'radius error' 'texture error' 'perimeter error' 'area error'
 'smoothness error' 'compactness error' 'concavity error'
 'concave points error' 'symmetry error' 'fractal dimension error'
 'worst radius' 'worst texture' 'worst perimeter' 'worst area'
 'worst smoothness' 'worst compactness' 'worst concavity'
 'worst concave points' 'worst symmetry' 'worst fractal dimension']
"""

# we split the data into train and test
# the data is t he feature data, and the target is the target
x_train, x_test, y_train, y_test = train_test_split(np.array(data.data), np.array(data.target), test_size=0.2)
# We're saying take the data, all the parameters of the features (rows and values),
#  put them in a np.array, then also take, all the results/classifications/targets
#  and put them in another np.array, and then split the data (it also shuffles it randomly)

# we define the classifier with 3 neighbors as we have 2 target classes 
clf = KNeighborsClassifier(n_neighbors=3)
# we fit the data
clf.fit(x_train, y_train)

# evaluating the performance of the model
print("classifier score: ", clf.score(x_test, y_test))
# classifier score:  0.9210526315789473


# to test real world data you pass np.array of all the parameters
#  and then it classifies them whether malignant or benign
#  we don't got data tho
clf.predict()