from dataclasses import dataclass
from math import inf

@dataclass
class algorithm():
    '''
    The idea is to recursively get the minimum number and then add it to the 
    sorted elements. You won't need to sort this selected number in the sorted
    list because in that part of the list everything is already minimum compared
    with the last chosen element.
    '''

    @staticmethod
    def selection_sort(l):
        for i in range(len(l)):
            index_min=elem_min=inf
            for j in range(i,len(l)):
                if l[j]<elem_min:
                    index_min=j                
                    elem_min=l[j]
            l[i],l[index_min]=elem_min,l[i]
            print(l)
        return l

L=[1,5,3,0,2,9,4,7,6,8]
print("Original:",L)
print("Result:  ",algorithm.selection_sort(L))
