import numpy as np
A=[3,4,4,6,1,4,4]

def sol(n,A):
    res=np.zeros(n)
    for i in range (len(A)) :
        if(A[i]>=1) and (A[i]<=n) :
            res[A[i]-1]+=1
        elif (A[i]== n+1):
            ma=max(res)
            res=[ma]*n
    print(res)

sol(5,A)
