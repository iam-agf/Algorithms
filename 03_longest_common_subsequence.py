from dataclasses import dataclass

@dataclass
class algorithm():

    @staticmethod
    def lcsTable(str1,str2):
        '''
        The main idea is to generate a table using Dynamic programming and fill
        it with the longest subsequence obtained from the path you're coming 
        from. In the double loop, the if imply you're coming from a path where 
        you achieved a common char. On the other side the else means that in 
        this step you didn't get a match between the char of str1 and str2.
        '''

        n,m=len(str1),len(str2)
        dyn_table=[[0]*(m+1) for _ in range(n+1)]

        for j in range(n):
            for k in range(m):
                if str1[j]==str2[k]:
                    dyn_table[j+1][k+1]=dyn_table[j][k]+1
                else:
                    dyn_table[j+1][k+1]=max(dyn_table[j][k+1],dyn_table[j+1][k])
        
        return dyn_table
        

    @staticmethod
    def longestCommonSubsequence(str1,str2):
        '''
        Here the main idea is to use the table we built in lcsTable to recover
        the solution we found. We will backtrack the path to achieve the chars
        that match between the strings, and finally we will reverse the string,
        since originally we're doing a backtrack in the table.
        '''
        dyn_table=algorithm.lcsTable(str1,str2)
        solution=[]
        j,k=len(str1),len(str2)
        while dyn_table[j][k]>0:
            if str1[j-1]==str2[k-1]: 
                solution.append(str1[j-1])
                j-=1
                k-=1
            elif dyn_table[j-1][k]>=dyn_table[j][k-1]:
                j-=1
            else:
                k-=1
        return ''.join(reversed(solution))

print(algorithm.longestCommonSubsequence("GTTCCTAATA","CGATAATTGAGA"))
