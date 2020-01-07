"""
--> defaultdict takes function as argument which return the default value of the key, which is not exist in the dict
Examples:
>>character_occurrences = defaultdict(list)
>>character_occurrences['a']
[]

>>character_occurrences = defaultdict(int)
>>character_occurrences['a']
0

>>character_occurrences = defaultdict(float)
>>character_occurrences['a']
0.0

"""
from collections import defaultdict


def defaultvalue():
    return 0

otherdict = defaultdict(defaultvalue)
otherdict['a'] = 1
otherdict['d']
print(otherdict)

