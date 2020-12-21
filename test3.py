def solution(A):
    L= len(A)
    M=0
    for i in range(L):
        A[i] = abs(A[i])
        M = max(A[i], M)
    S = sum(A)
    c = [0] * (M + 1)
    for i in range(L):
        c[A[i]] += 1
    x = [-1] * (S + 1)
    x[0] = 0
    for a in range(1, M + 1):
        if c[a] > 0:
            for j in range(S):
                if x[j] >= 0:
                    x[j] = c[a]
                elif (j >= a and x[j - a] > 0):
                    x[j] = x[j - a] - 1
    result = S
    for i in range(S // 2 + 1):
        if x[i] >= 0:
            result = min(result, S - 2 * i)
    print(result)

solution([1,5,2,-2])
