# K-Means Clustering - unsupervised learning algorithm

"""
We once again draw a graph/ coordinate system with data points
 all data points are grey but they're clustered around the graph
 because it's unsupervised we have no classification for training.
We just say "these are the points, I want you to find a K-amount of clusters"
 - K-Means CLustering
 just train the model on the data and assign clusters
 the data in real life isn't as clear as the 2D example of 3 clearly distinct clusters
 we can have 20+D different features / dimensions

We can't just say look at the data, we need an algorithm
 we define the K = 3, which means we start with 3 'centroids'
 centroid - center/centers of a cluster, these centroids are random,
  we don't choose or place them
 then we look at all of the data points and look at which centroid is it closest to

    image 1: '#6 - clusters.png'

This right now isn't accurate, we do an iteration, we move the centroids to the
 middle of the points (average of distances from points). Then we do the same again,
 we check all data points and their distance to the centroids and assign colors/clusters
 Rinse and repeat...

    image 2: '#6 - cluster iteration.png'

In the end we end up with the optimal centroids that are in the middle of the points,
 / when we see that the iterations result in very small changes
 (the way I see it combinas error loss pa K-Nearest algorithms for from scratch implementation)
"""

from sklearn.cluster import KMeans
from sklearn.preprocessing import scale     # to normalise data from 0 to 1
from sklearn.datasets import load_digits    # handwritten digits scanned
# we can use this dataset to classify them, but in this case we're just gonna cluster them
# pictures from 0-9 and we're just putting them in groups without labeling them
# we're just giving the model the pixels no labels

digits = load_digits() # loading the image pixel arrays
#print(digits)
data = scale(digits.data) # normalising just the data of the digits (you also have descriptions in there)
#print(data)


# n_clusters <- we specify how many clusters we want, in this case digits from 0-9 we need 10 clusters
# init <- method how to determine starting points of centroids, we use 'random'
# n_init <- how many times should it start with different initialisations/ different initial centroids
model = KMeans(n_clusters=10, init='random', n_init=10)
model.fit(data)


# it doesn't really make sense to test this, because this is unsupervised learning
# we don't have a measure of true or false, we just have clusters
# we can just put in new pixels to try /future video)
#model.predict([...])

# we can just read in a picture of a handwritten number and it will just put it 
#  in a cluster, but we cant say this is a 7 and so we cant say whether its true or false
#  just what the model says
# the only measure of accuracy would be "how well are the centroids placed"
#  a.k.a. what are the distances to the centroids of the clusters to each point in the cluster
#  if the distance is small then the clusters are well formed, if they're large something is amiss