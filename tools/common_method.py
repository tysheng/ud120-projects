# -*- coding: utf-8 -*-
"""
@description:
@author: tysheng
@email: tyshengsx@gmail.com
@time: 2017/8/11 23:11
"""

import time


def do_with_clf(clf, lessen=False, certain_num=None):
    from tools.email_preprocess import preprocess

    ### features_train and features_test are the features for the training
    ### and testing datasets, respectively
    ### labels_train and labels_test are the corresponding item labels

    time_ = time.time()
    features_train, features_test, labels_train, labels_test = preprocess()
    print('产生数据时间：', time.time() - time_)
    do_with_data(clf, features_train, features_test, labels_train, labels_test, lessen, certain_num)


def do_with_data(clf, features_train, features_test, labels_train, labels_test, lessen=False, certain_num=None):
    print('features size: ', len(features_train[0]))

    if lessen:
        features_train = features_train[:len(features_train) // 100]
        labels_train = labels_train[:len(labels_train) // 100]
    time_ = time.time()
    clf.fit(X=features_train, y=labels_train)
    pred = clf.predict(features_test)
    if certain_num is not None:
        for num in certain_num:
            print(pred[num])
    # count = 0
    # for num in pred:
    #     if num == 1:
    #         count += 1
    # print(count)
    from sklearn import metrics

    accu = metrics.accuracy_score(y_true=labels_test, y_pred=pred)
    # print(pred)
    print('accuracy_score: ',accu)
    print('处理数据时间：', time.time() - time_)
