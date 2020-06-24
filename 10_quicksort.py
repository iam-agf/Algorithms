from dataclasses import dataclass
from math import inf

'''
Code obtained from: 
https://stackoverflow.com/questions/18262306/quicksort-with-python
It's more clear than mine, so I decided it's better, since the idea
is to have a library of the algorithms in the list in the README.
'''

@dataclass
class algorithm():


    @staticmethod
    def quicksort(l):
        """Gets a pointer and splits the arrays in:
        
        +Elements less than the pointer
        +Elements equal to the pointer
        +Elements greater than the pointer
        
        And after it, it's done recursively until the arrays are of size 1."""

        less = []
        equal = []
        greater = []
        if len(l) > 1:
            pivot = l[0]
            for x in l:
                if x < pivot: less.append(x)
                if x == pivot: equal.append(x)
                if x > pivot: greater.append(x)
            return algorithm.quicksort(less)+equal+algorithm.quicksort(greater)  
        else:  
            return l
#L=[7,2,8,1,3,4,10,6,9,5]
L=[0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]

print(algorithm.quicksort(L))