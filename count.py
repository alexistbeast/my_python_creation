
def count(s):
    count_dict = {char: 0 for char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    for i in s:
        if i in count_dict.keys():
            count_dict[i] += 1
    result = {}
    for keys,values in count_dict.items():
        if values > 0:
            result[keys] = values
    return result