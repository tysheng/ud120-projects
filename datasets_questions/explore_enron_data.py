#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
# enron_name = pickle.load(open("../final_project/poi_name.txt", "rb"))
# enron_data = dict(enron_data)
# print(enron_data)
count = 0
for k, v in enron_data.items():
    # v=dict(v)
    if True:#"SKILLING JEFF" in k
        # print(v)

        if v['total_payments'] == 'NaN':
            count+=1
        # for k_,v_ in v.items():
        #     if 'total_payments' in k_:
        #         print(k_,v_)

print(count)
print(count/len(enron_data))
