#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""

#########################################################
### your code goes here ###
import sklearn.svm as svm

clf = svm.SVC(C=10000)

import tools.common_method as cm

"""
    parameter:
    c , 
    gamma ,
    kernel: rbf is very slow
    

"""
# cm.do_with_clf(clf, True,(10, 26, 50))
cm.do_with_clf(clf)

#########################################################
"""
no. of Chris training emails: 7936
no. of Sara training emails: 7884
0.98976109215

缩小到 1/100
    linear 0.898179749716
    rbf 0.616040955631
        C:  10: 0.616040955631
            100: 0.616040955631
            1000: 0.821387940842
            10000: 0.892491467577
        不缩小 C=10000: 0.990898748578
"""
