def solution(A, B):

    T = max(A)


    f= [0] * (T+2)

    f[1] = 1

    for i in range(2, T + 2):

        f[i] = f[i - 1] + f[i - 2]


    res = [0] * len(A)


    for j in range(len(A)):

        res[j] = f[A[j]+1] & ((1 << B[j]) - 1)
        
    print (res)

A=[4,4,5,5,1]
B=[3,2,4,3,1]

solution(A,B)
