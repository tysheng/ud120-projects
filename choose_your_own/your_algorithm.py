#!/usr/bin/python

import matplotlib.pyplot as plt
from choose_your_own.prep_terrain_data import makeTerrainData
from choose_your_own.class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

"""
knn stuff
"""

from sklearn.neighbors import KNeighborsClassifier
import tools.common_method as cm
clf = KNeighborsClassifier()

cm.do_with_data(clf,features_train, features_test,labels_train, labels_test)
# def prettyPicture(clf, features_test, labels_test):
#     pred =clf.predict(features_test)
#     import sklearn.metrics as sm
#     accu = sm.accuracy_score(y_true=labels_test,y_pred=pred)
#     print(accu)

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
