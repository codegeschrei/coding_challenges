def dict_merge(dict1, dict2, decision_func=None):

    if not decision_func:
        # if the keys of dict1 always have higher priority always update dict2 first
        merge = {}
        merge.update(dict2)
        merge.update(dict1)
        return merge
    else:
        merge = {}
        merge.update(dict2)
        merge.update(dict1)
        keys = [x for x in dict1 if x in dict2]
        # I guess this could be written as list comprehension but I prefer fast readable code
        for key in keys:
            try:
                merge[key] = decision_func(dict1[key], dict2[key])
            except TypeError:
                # depending on the function used in decision_func the exceptions will differ
                # in this case we assume we use the sum function and nothing else
                return 'Please check your dictionaries according to your decision_func'
        return merge


# not calling it 'sum' because of overshadowing
def decision_func_sum(x, y):
    return x + y
