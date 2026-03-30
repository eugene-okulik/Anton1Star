my_dict = {
    'tuple': (1, 2, 3, 3.5, 5, 'Hello'),
    'list': [1, 2, 3, 3.5, 5, 'Hello', None],
    'dict': {'one': 1, 'two': 'apple', 'three': 'chees', 'four': 2, 'false': 3},
    'set': {1, 2, 3, 3.5, 5, 'Hello'},
}

print(my_dict['tuple'][-1])

my_dict['list'].pop(1)
my_dict['list'].append(1)

my_dict['set'].add(4.5)
my_dict['set'].discard(3)

my_dict['dict']['i am a tuple',] = 'nope'
del my_dict['dict']['false']

print(my_dict)
