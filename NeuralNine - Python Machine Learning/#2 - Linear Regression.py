# Linear Regression - supervised learning

# in depth blog post
# https://www.neuralnine.com/linear-regression-from-scratch-in-python/


# no deep mathematics just implementation with scikit and tensorflow

# we have data with some error / deviation
# we're trying to find the optimal function with the least error to the data points
# we're adjusting the f(x) = m*x + b, a,b parameters
# the mean squared error, we're minimizing that
# you can overfit the model which has 100% accuracy but a new data point would screw it up

# there's always some error
# linear models become powerful when we operate in higher dimensions, 
#  i.e. 20 features, and then train linear model
# when we have a 3D space, then the linear model represents a hyperplane
# linear just means flat, in 2D - line, in 3D - plane, 4+D - hyperplane

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import random


# we need some data first, he did it mannually cause retard
time_studied = np.array([20, 50, 32, 65, 23, 43, 10, 5, 22, 35, 29, 5, 56])
scores = np.array([56, 83, 47, 93, 47, 82, 45, 78, 55, 67, 57, 4, 12])

"""
# my data
time_studied = np.linspace(0, 70, 1000)
err = np.array([random.uniform(-50, 50) for _ in range(len(time_studied))])
scores = abs(np.linspace(0, 100, 1000)+err)
#print(time_studied)
#print(scores)
"""

# we need to invert/transpose the arrays for scikitlearn (it needs vectors)
# we do that by using  .reshape(-1, 1)
time_studied = time_studied.reshape(-1, 1)
scores = scores.reshape(-1, 1)


# now we create model and train it
model = LinearRegression()
model.fit(time_studied, scores)


# we can predict the value
print(model.predict(np.array([56]).reshape(-1, 1)))
# [[68.22055244]]


# visualization
#plt.scatter(time_studied, scores)
t = np.linspace(0, 70, 100).reshape(-1, 1)
#plt.plot(t, model.predict(t), 'r')

plt.ylim(0, 100)
#plt.show()
plt.clf


# testing the model
# we trained the model and used it, we don't know how accurate it is,
#  how well it performs
# you want to take aside 80% of data for training and 20% for testing

from sklearn.model_selection import  train_test_split
# for splitting data into training and testing data

# we removed the outlier because they ruin the accuracy on a low data sample
time_studied = np.array([20, 50, 32, 65, 23, 43, 10, 5, 22, 35, 29, 5, 56]).reshape(-1, 1)
scores = np.array([56, 83, 47, 93, 47, 82, 45, 23, 55, 67, 57, 4, 89]).reshape(-1, 1)

time_train, time_test, score_train, score_test = train_test_split(time_studied, scores, test_size=0.3)

model = LinearRegression()
model.fit(time_train, score_train)

# here we're testing on the 20%
print(model.score(time_test, score_test))
# 0.9750431024155146
# 0.651763753476291
# 0.6788650645379295

plt.scatter(time_train, score_train)
t = np.linspace(0, 70, 100).reshape(-1, 1)
plt.plot(t, model.predict(t), 'r')
plt.show()


# the train_test_split takes a random split from your data 
#  (so if you have 10 points and make the test_size=0.1 - 10% it gives you one point for testing) 
# and because the point is random it tests the accuracy of the model with these points