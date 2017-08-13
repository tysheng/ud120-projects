#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""




#########################################################
### your code goes here ###

from sklearn import tree

clf = tree.DecisionTreeClassifier(min_samples_split=50)

import tools.common_method as cm

cm.do_with_clf(clf)

#########################################################


"""
1%的数据: 0.964163822526



"""