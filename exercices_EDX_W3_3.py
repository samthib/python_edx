# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 23:20:47 2020

@author: Sam
"""


import numpy as np, random, scipy.stats as ss

def majority_vote_fast(votes):
    mode, count = ss.mstats.mode(votes)
    return mode

def distance(p1, p2):
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))

def find_nearest_neighbors(p, points, k=5):
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    ind = np.argsort(distances)
    return ind[:k]

def knn_predict(p, points, outcomes, k=5):
    ind = find_nearest_neighbors(p, points, k)
    return majority_vote_fast(outcomes[ind])[0]


# Exercice 1
    
import pandas as pd

# Read the file and create the DataFrame 
data = pd.read_csv("asset-v1_HarvardX+PH526x+2T2019+type@asset+block@wine.csv", index_col=0)

#print(data)

# Exercice 2

# create a new column
data.loc[data["color"] == 'red', "is_red"] = 1  
data.loc[data["color"] == 'white', "is_red"] = 0
# drop a column
del data['color']
# Print the DataFrame after addition of new column 
numeric_data = data
#print(numeric_data)
#print(sum(data["is_red"]))

# Exercice 3

import sklearn.preprocessing
scaled_data = sklearn.preprocessing.scale(numeric_data)
numeric_data = pd.DataFrame(scaled_data, columns = numeric_data.columns)

import sklearn.decomposition
pca = sklearn.decomposition.PCA(n_components=2)
principal_components = pca.fit_transform(numeric_data)

#print(principal_components)
#print(np.shape(principal_components))

# Exercice 4

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.backends.backend_pdf import PdfPages
observation_colormap = ListedColormap(['red', 'blue'])
x = principal_components[:,0]
y = principal_components[:,1]

plt.title("Principal Components of Wine")
plt.scatter(x, y, alpha = 0.2,
    c = data['high_quality'], cmap = observation_colormap, edgecolors = 'none')
plt.xlim(-8, 8); plt.ylim(-8, 8)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.show()


# Exercice 5

np.random.seed(1) # do not change

x = np.random.randint(0, 2, 1000)
y = np.random.randint(0, 2, 1000)

def accuracy(predictions, outcomes):
    n = len(predictions)
    k = len(outcomes)
    if n != k:
        return "different array sizes"

    equal_count = 0
    for i in range(n):
        if predictions[i] == outcomes[i]:
            equal_count += 1
      
    ratio = 100 * equal_count / n 

    return ratio

#print(accuracy(x, y))
    

# Exercice 6

zeros_list = np.zeros(len(data["high_quality"]))
#print(accuracy(zeros_list, list(data["high_quality"])))


# Exercice 7

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(numeric_data, data['high_quality'])

library_predictions = knn.predict(numeric_data)

#print(accuracy(library_predictions, list(data['high_quality'])))
    
      
# Exercice 8

n_rows = data.shape[0]

random.seed(123)
selection = random.sample(range(n_rows), 10)

#print(selection)


# Exercice 9

predictors = np.array(numeric_data)
training_indices = [i for i in range(len(predictors)) if i not in selection]
outcomes = np.array(data["high_quality"])

my_predictions = []
for p in predictors[selection]:
    my_predictions.append(knn_predict(p, predictors[training_indices,:], outcomes, k=5))
    
#percentage = # Enter your code here!

print(my_predictions)
#for select in data.high_quality[selection]
print(selection)
#for prediction in my_predictions:
 #   percentage = accuracy(my_predictions, data.high_quality[selection])
    
#print(percentage)
#print(data.high_quality[selection])
