from dataclasses import dataclass
from math import inf

@dataclass
class algorithm():

    @staticmethod
    def selection_sort(A):
        for i in range(1,len(A)):
            for j in range(i,0,-1):
                if A[j]<A[j-1]:
                    A[j],A[j-1]=A[j-1],A[j]
                print(">>",A)
        return A
L=[6,5,3,1,8,7,2,4]
print("Original:",L)
print("Result:  ",algorithm.selection_sort(L))