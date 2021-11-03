dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'z': 6, 'y': 8, 'w': 4}
print(dict2.items())
print(dict2.values())
new_dict_k = {k: v for k, v in sorted(dict2.items())}
new_dict_v = {k: v for k, v in sorted(dict2.items(), key=lambda x: x[1])}
print(new_dict_k)
print(new_dict_v)