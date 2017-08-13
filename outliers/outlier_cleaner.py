#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    # cleaned_data = []

    ### your code goes here
    # print(predictions,ages,net_worths)
    size_ = len(predictions)
    print(size_)
    abs_ = map(lambda x: x ** 2, predictions - net_worths)
    map_ = zip( ages, net_worths,abs_)
    # 按第三个元素排序
    sorted_ = sorted(map_, key=lambda tup: tup[2])
    cleaned_data =sorted_[0:-int(0.1 * size_)]
    print(len(cleaned_data))
    return cleaned_data
