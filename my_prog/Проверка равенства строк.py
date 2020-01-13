# Проверка равенства строк
A = str(input('Текст1: '))
B = str(input('Текст2: '))
def equal(A, B):
    if len(A) != len(B):
        return False
    for i in range(len(A)):
        if A[i] != B[i]:
            return False
    return True
print(equal(A, B))
