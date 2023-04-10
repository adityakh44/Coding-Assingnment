import numpy as np

integer = int(input("Enter the number :- "))
vector = input("Enter vector values :- ").split()
vec = np.array(vector)

def countOccurrences(vec, n, integer):
    res = 0
    
    for i in range(n):

        if integer == vec[i]:

            res += 1

    return res

n = len(vec)

print(" Vector = " , vec)
print(" count = " , countOccurrences(vec, n, integer))

    
        
    