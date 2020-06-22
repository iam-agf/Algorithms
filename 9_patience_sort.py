from dataclasses import dataclass
from math import inf

@dataclass
class algorithm():

    @staticmethod
    def patienceSort(l):
        solitaire_stacks=[]
        for i in l:
            inserted=False
            for stack in solitaire_stacks:
                if not inserted:
                    if stack[-1]>=i:
                        stack.append(i)
                        inserted=True
                if inserted: break 
            if not inserted:
                solitaire_stacks.append([i])
            print(solitaire_stacks)
            
        return solitaire_stacks
#L=[7,2,8,1,3,4,10,6,9,5]
L=[0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]

print(algorithm.patienceSort(L))