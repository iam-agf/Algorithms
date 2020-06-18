from dataclasses import dataclass

@dataclass
class algorithm():

    @staticmethod
    def binarySearch(checkingList,param):
        not_found=True
        step=0
        
        left_lim,right_lim=0,len(checkingList)
        
        while not_found:
            step+=1
            pointer=(left_lim+right_lim)//2
        
            if checkingList[pointer]>param: right_lim=pointer-1
            elif checkingList[pointer]<param: left_lim=pointer+1
            else: return pointer,step 

            print(left_lim,right_lim)

        return "didn't found the value {}".format(param)
        
print(algorithm.binarySearch(list(range(1000000)),2020))
