"""
python collection module is use to improve the functionality of the built-in collection container.
python built in collection containers are.
1. list
2. tuple
3. dict
4. set

Below are the collection module.
1. Counter
2. defaultdict
3. OrderdDict
4. deque
5. ChainMap
6. namedtuple
"""
from collections import Counter

"""
---> Counter is the subclass of dictionary object
---> it takes iterable as the argument and returns the dictionary
"""
l1 = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 2, 3, 3]

cnt = Counter(l1)                  # creating the counter object by passing l1 iterable
print(cnt)                         # the list value becomes keys and it count becomes value o/p
# o/p Counter({3: 4, 2: 3, 1: 2, 4: 2, 5: 1, 6: 1})

print(cnt[1])                      # accessing counter items with its key value  o/p 2

"""
counter had three editional features
1. elements()()
2. most_common()
3. subtract([iterable of mapping])
"""

m = list(cnt.elements())           # cnt.elements() will return the iterator object apply list to get the elements
print(m)                           # it will list all the elements o/p [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 6]

n = cnt.most_common()              # it will return list of tuple of most common elements and its count
print(n)                           # o/p [(3, 4), (2, 3), (1, 2), (4, 2), (5, 1), (6, 1)]


deduct = {1:2, 2:2}
cnt.subtract(deduct)              # it will subtract the count of the key value using the mapping dictionary.
print(cnt)                        # and update the same cnt object o/p Counter({3: 4, 4: 2, 2: 1, 5: 1, 6: 1, 1: 0})
