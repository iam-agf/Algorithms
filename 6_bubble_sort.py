from dataclasses import dataclass

@dataclass
class algorithm():

    @staticmethod
    def insertion_sort(l):
        for i in range(len(l)):
            for j in range(i,0,-1):
                if l[j]<l[j-1]:
                    l[j-1],l[j]=l[j],l[j-1]
                print(l)
        return l

L=[1,5,3,0,2,9,4,7,6,8]
print(algorithm.insertion_sort(L))