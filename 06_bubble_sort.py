from dataclasses import dataclass

'''
The point in each iteration is to get the biggest element and get it to the top
of the array. This iteration will be done n times.
'''
@dataclass
class algorithm():

    @staticmethod
    def bubble_sort(l):
        for i in range(len(l)):
            for j in range(1,len(l)-i):
                if l[j]<l[j-1]:
                    l[j-1],l[j]=l[j],l[j-1]
                print(l)
        return l

L=[8,5,3,0,2,9,4,7,6,1]
print(algorithm.bubble_sort(L))