#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""

#########################################################
### your code goes here ###
from sklearn.naive_bayes import GaussianNB

clf = GaussianNB()
import tools.common_method as cm
cm.do_with_clf(clf)

#########################################################
"""
no. of Chris training emails: 7936
no. of Sara training emails: 7884
[0 0 1 ..., 1 0 0]
0.973265073948

"""
