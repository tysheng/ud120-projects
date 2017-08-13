#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot

sys.path.append("../tools/")
from tools.feature_format import featureFormat, targetFeatureSplit

### read in data dictionary, convert to numpy array
data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

"""
TOTAL is the answer for 8.15
"""
data_dict.pop('TOTAL')
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)
print(data_dict)

### your code below

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter(salary, bonus)

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
# matplotlib.pyplot.show()

for k, v in data_dict.items():
    if float(v['salary']) > 1e6 and float(v['bonus']) > 5e6:
        print(k)
