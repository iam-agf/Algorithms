from dataclasses import dataclass

@dataclass
class algorithm():

    @staticmethod
    def compute_prefix(string1):
        m=len(string1)
        prefix_coincidences=[0] # We define the first comparation as zero

        for q in range(1,m):
            j=prefix_coincidences[q-1]
            while j>0 and string1[j]!=string1[q]:
                j=prefix_coincidences[j-1]
            prefix_coincidences.append(j+1 if string1[j]==string1[q] else j)
        return prefix_coincidences

    @staticmethod
    def KnuthMorrisPratt_match1(string1,pattern):
        n,m=len(string1),len(pattern)
        if m==0: return 0

        restarts=algorithm.compute_prefix(pattern)
        j,k=1,0

        while j<n:
            if string1[j]==pattern[k]:
                if k==m-1:
                    return(j-m+1)
                j+=1
                k+=1
            elif k>0:
                k=restarts[k-1]
            else: j+=1
        return -1

    @staticmethod
    def KnuthMorrisPratt(string1,pattern):
        n,m=len(string1),len(pattern) 
        if m==0: return 0 # If the len of pattern is 0, we end

        restarts=algorithm.compute_prefix(pattern) # Prefix table
        j,k=0,0 

        while j<n:
            if string1[j]==pattern[k]:
                if k==m-1:
                    print(j-m+1)
                    k=restarts[k-1]
                j+=1
                k+=1
            elif k>0:
                k=restarts[k-1]
            else: j+=1
        return


algorithm.KnuthMorrisPratt('ezgonzalez fernandez ez','ez')