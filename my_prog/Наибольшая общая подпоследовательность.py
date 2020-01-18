# Динамическое программирование

def lcs(A, B):

    '''Функция наибольшей общей последовательности (длина)'''
    
    F = [[0] * (len(B)+1) for i in range(len(A)+1)]
    for i in range(len(A)+1):
        for j in range(len(B)+1):
            if A[i-1] == B[j-1]:
                F[i][j] = 1 + F[i-1][j-1]
            else:
                F[i][j] = max(F[i-1][j], F[i][j-1])
    return F[-1][-1]

A = [1,6,4,7,32,67]
B = [0, 3,4,7,32,54]

print(lcs(A,B))


def gis(A):

    '''Функция наибольшей возрастающей последовательности (длина)'''
    
    F = [0] * (len(A) + 1)
    for i in range(1, len(A) + 1):
        m = 0
        for j in range(0, i):
            if A[i-1] > A[j-1] and F[j-1] > m:
                m = F[j]
        F[i] = m + 1
    return F[len(A)]

print(gis([1,2,3,4,5]))



