# Decision Trees Classifier and Random Forest Classifier


# Decision Tree Classification _________________________________________________
"""
Imagine we have a person called Mark and Mark has a decision to make
 "is he going into nature or not?"
 We have to predict his decision with historical data that we have
 Multiple historical events whether he went to nature or not
 
 the data that we have:
 time & choice & weather & was he alone   <--  these are our different parameters
 1  Y   Y   N   Y
 2  Y   Y   Y   N
 3  N   Y   Y   Y
 4  N
 5  Y
 ...

We have this dataset of events of did he go out or not, and we try to build a 
 Decision Tree model that predicts answers, we give it parameters, and it predicts

We would have a ROOT (i.e. Sunny, not Sunny) then it splits into two branches 
 for example (rain vs no rain in the not Sunny tree) and so on and so forth

    image 1: '#5 - tree.png'
  
We can also have more classifications not just binary yes or no

How is this model trained in Python. In the begginning we define the Root node,
 which asks 1 question, random feature, and we split up the possibilities into 
 different branches. 
 Then we use the dataset from the beginning and we extrapolate wether the circumstances match
 We check for all the data rows that end up being a Y or N in the final summation
 for example if sunny Y:85 and N:0  then he obviously goes
 if not sunny Y:30 and N:55 then we ask the next question, is it rainy or not
 we again get for Yes possibility how many outcomes lead to Y and how many to N
 and the same for No possibilities 
 so now if its not sunny and not raining we have N:40 and Y:0 and we decide N
 for the not sunny not raining we ask further is he alone, and so on...

In the end we end up with a model thats trained, it takes the data and optimizes the decision tree
 but of course we have a random factor, which feature do we start with, makes a difference
 you can have multiple trees with different outcomes/efficiencies.
"""

# Random Forest Classification _________________________________________________
"""
This is where the random forest classification comes into play, because a decision
 tree might be kind of random because of the order of the features
 if we have like 50 features the order of the features chose is very important
 and might lead to huge differences in the output

What we do with the Random Forest Classification, is we create multiple trees
 like a 100 decision trees and train all of them on the same data, forest made
 up of multiple trees trained on the same data
Then we get a new test example and feed it into all of the decision trees in the forest
 and they will all give me an answer/output, 
 if we have 4 trees and 3 output Y and 1 outputs N the collective prediction is Y

We train multiple trees to have different opinions on the same issue,
 with this we minimize the risk of missclassification. "Democratic system"
"""

# the focus of these initial episodes is to get to know as many algorithms
#  and classifications as possible, and later get into deeper topics

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC     # SVC - Support Vector Classifier
from sklearn.neighbors import KNeighborsClassifier # for comparison of accuracy

from sklearn.tree import DecisionTreeClassifier         # Decision Tree
from sklearn.ensemble import RandomForestClassifier     # Random Forest
# DecisionTreeRegressor and RandomForestRegressor work the same


data = load_breast_cancer()

X = data.data
Y = data.target

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)


clf1 = SVC(kernel='linear', C=3)
clf1.fit(x_train, y_train)

clf2 = KNeighborsClassifier(n_neighbors=3)
clf2.fit(x_train, y_train)

clf3 = DecisionTreeClassifier()
clf3.fit(x_train, y_train)

clf4 = RandomForestClassifier() # we can also define specifics and adjust the model
clf4.fit(x_train, y_train)

# scoring it
print(f'SVC: {clf1.score(x_test, y_test)}') # SVC: 0.9473684210526315
print(f'KNN: {clf2.score(x_test, y_test)}') # KNN: 0.9210526315789473
print(f'DTC: {clf3.score(x_test, y_test)}') # DTC: 0.9210526315789473
print(f'RFC: {clf4.score(x_test, y_test)}') # RFC: 0.956140350877193
# the RFC is better in these cases (also a bit random).
# on average the same accuraccy, RFC or SVC best
# for him in the vid SVC won most times, for me RFC wins.