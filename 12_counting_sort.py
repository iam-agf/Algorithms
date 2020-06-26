from dataclasses import dataclass
from collections import Counter

@dataclass
class algorithm:
    '''
    Counting sort uses a list that saves how many repetitions are of each 
    element in the array and then returns the list sorted. In this case we can 
    approach in two ways: using a dictionary (in fact from collections we can 
    use the structure Counter) and the basic method that is following the 
    algorithm in a strict way.  
    '''

    @staticmethod
    def CounterSort(l):
        C=Counter(l)
        A=[]
        for i in sorted(C.keys()):
            for j in range(C[i]):
                A.append(i)
        return A

    @staticmethod
    def countingSort(l):
        M=max(l)
        A=[0]*(M+1)
        for i in l:
            A[i]+=1
        ans=[]
        for i in range(len(A)):
            for j in range(A[i]):
                ans.append(i)
        return ans

print(algorithm.countingSort([1,1,3,2,3,5,3,3,5,7,8,1,2,3,6,1,5,2]))
print(algorithm.countingSort([1,1,3,2,3,5,3,3,5,7,8,1,2,3,6,1,5,2])==algorithm.CounterSort([1,1,3,2,3,5,3,3,5,7,8,1,2,3,6,1,5,2]))