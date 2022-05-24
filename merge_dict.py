one = {'a': '1', 'b': '2'}
two = {'c': '3', 'a': '4'}
merged = {}
def merge_dict(one, two):
    for i in one:
        if i in two:
            merged[i] = [one[i], two[i]]
        else:
            merged[i] = one[i]

    for i in two:
        if i not in one:
            merged[i] = merged[i]
    return merged
        

print(merge_dict({'a': '1', 'b': '2'},{'c': '3', 'a': '4'} ))