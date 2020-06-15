from dataclasses import dataclass

'''
The main idea of the algorithm is to hash each substring with the same size that
has pattern and check if both have the same value. If it finds it, it ends.
'''

@dataclass
class algorithm():

    @staticmethod
    def RabinKarp(pattern,string):
        '''
        Complexity time O(n)
        
        The function will return the starting index where the string matches
        and the final index where it finishes. It won't detect lower or upper
        cases.
        '''

        bs_len=len(string)
        p_len=len(pattern)

        for i in range(bs_len-p_len+1):
            if hash(pattern) ==hash(string[i:i+p_len]):
                return(i,i+p_len-1) # i+p_len-1 is the last index that matches.


print(algorithm.RabinKarp("ame","and his name is John Cena"))