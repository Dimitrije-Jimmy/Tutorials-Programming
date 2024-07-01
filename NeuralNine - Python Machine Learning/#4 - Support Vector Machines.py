# Support Vector Machines
# very powerful tools for classifying data by using support vectors,
#  in some cases they outperform Neural Networks, for example 'Handwritten Digits' example
#  (in this specific example convolutional neural network that specializes in image data still wins)

"""
Once again we imagine a graph with feature2 in relation to feature1
 we have two clusters one with red dots one with blue
 instead of like K-Nearest Neighbors calculation of distance.
With Support Vector Machines we train a mathemathical linear function to split the data
 a line that splits data/clusters in the most optimal/generalised way
 we have an infinite amount of ways of drawing the line, but the most optimal one,
 is the one that is the furthest away from all points.
To find this line we use a support vector (in imae marked green), which is a
 prallel line from the baseline. The green area is called the margin area -
 - it's the space where there are no points in it.
 and it should be the same from both sides.

    image 1: '#4 - support vector.png'

We use the line to classify future data

The data in real life is never that structured, you can spot the classes
 but they're more intertwined/overlapping and you can no longer split it with a line
We have to find a different way of classifying, we use a concept of Kernels - jedra
 Kernels add a third dimension/ additional dimension, if we have F1 and F2 we add
 an additional dimension so that we can use a hyperplane to separate data
 we have flat data and we lift it up into the third dimension,
 we're not allowed to add in new data we're just making it more redundant
 we combine F1 and F2 to get the K/ F3 value (F3 = F1 + F2 doesn't make sense)
 we use predefined Kernel functions that are optimized.

    image 2: '#4 - kernels.png'

Soft Margin - like a tolerance, marging of error as there are outliers,
 we allow a missclassification up to a certain number of data points,
 to get the best line (just think fitting and not overfitting)  
"""

# the actual code is not that different to K-Neighbors Classification
#  we're just changing the model, we're not implementing the mathemathics ourselves

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC     # SVC - Support Vector Classifier
from sklearn.neighbors import KNeighborsClassifier # for comparison of accuracy

data = load_breast_cancer()

X = data.data
Y = data.target


# if we want to always have the same state for the randomness (with reruns)
#  we att the 'random_state'='some_seed_number' (the seed can be whatever)
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

# defining the classifier
# we define the Kernel function and the Soft Margin
# the default for the Kernel is 'rbf' but it takes a lot of time, 
#  we laso have the 'polynomial', ... and the fastest is the 'linear'
# 'C' parameter is for the Soft Margin
# this is the suport vector machine - the classifier
clf = SVC(kernel='linear', C=3)
clf.fit(x_train, y_train)  # training the model

# scoring it
print(f'SVC: {clf.score(x_test, y_test)}')  # 0.9473684210526315


# comparing it to the K-Neihgbors
clf2 = KNeighborsClassifier(n_neighbors=3)
clf2.fit(x_train, y_train)

print(f'KNN: {clf2.score(x_test, y_test)}')  # 0.9035087719298246

# they're roughly the same, depends on randomnness
#  with higher level data it makes a difference
"""
SVC: 0.9649122807017544
KNN: 0.9473684210526315
"""