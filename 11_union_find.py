from collections import defaultdict

class unionFind():
    __slots__=['content','track']

    def __init__(self,size):
        self.content=list(range(size+1)) #Each element is in its own family.
        self.track={i:set([i]) for i in range(size+1)} # Each set

    def union(self,a,b):
        # Gets the owner of the family with the smallest set of childs
        t=min(self.content[a],self.content[b],key=lambda x: len(self.track[x]))
        q=self.content[a]+self.content[b]-t

        to_update=self.track[t]
        self.track[q]=self.track[q].union(self.track[t])
        for i in to_update:
            self.content[i]=self.content[q]
        self.track.pop(t)

    def root(self,a):
        return self.content[a]
    
    def sameSet(self,a,b):
        return self.content[a]==self.content[b]

    def families(self):
        return len(set(self.content))


A=unionFind(10)

A.union(0,5)
A.union(6,5)
A.union(1,2)
A.union(7,2)
A.union(3,8)
A.union(4,9)
A.union(3,4)

for a in range(10):
    print("++++++++++++++++++++",a)
    for b in range(10):
        print(a,b,A.sameSet(a,b))

print(A.content)
print(A.track)