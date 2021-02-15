def RabinKarp(pattern, string, repetitions = False):
    '''
    Complexity time O(n)

    The function will return the starting index where the 
    string matches and where it finishes. It's case sensitive.

    The main idea of the algorithm is to compare the hash of 
    each substring with the same size that has pattern if both 
    have the same value. If it finds it, it ends.

    If you need the repetitions (repetitions = True), the 
    algorithm can save the indices when they substring matches 
    and continue checking the rest of the main string. In the end
    it will return a list of tuples (start, end) that define the
    positions for the substring that matches.
    '''

    string_len = len(string)
    pattern_len = len(pattern)

    if repetitions == True:
        indices = []
    for i in range(string_len-pattern_len+1):
        if hash(pattern) ==hash(string[i:i+pattern_len]):
            if repetitions == False:
                return(i,i+pattern_len-1) # i+p_len-1 is the last index that matches.
            else:
                indices.append((i,i+pattern_len-1))
    return indices
print(RabinKarp("ame","and his name is John Cena"))
