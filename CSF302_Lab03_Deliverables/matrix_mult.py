import random
import time

def traditional_multiply(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            for j in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def add(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def subtract(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

def strassen(A, B):
    n = len(A)
    if n <= 2:
        return traditional_multiply(A, B)

    m = n // 2
    A11 = [row[:m] for row in A[:m]]
    A12 = [row[m:] for row in A[:m]]
    A21 = [row[:m] for row in A[m:]]
    A22 = [row[m:] for row in A[m:]]
    B11 = [row[:m] for row in B[:m]]
    B12 = [row[m:] for row in B[:m]]
    B21 = [row[:m] for row in B[m:]]
    B22 = [row[m:] for row in B[m:]]

    M1 = strassen(add(A11, A22), add(B11, B22))
    M2 = strassen(add(A21, A22), B11)
    M3 = strassen(A11, subtract(B12, B22))
    M4 = strassen(A22, subtract(B21, B11))
    M5 = strassen(add(A11, A12), B22)
    M6 = strassen(subtract(A21, A11), add(B11, B12))
    M7 = strassen(subtract(A12, A22), add(B21, B22))

    C11 = add(subtract(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(subtract(add(M1, M3), M2), M6)

    return ([C11[i] + C12[i] for i in range(m)] +
            [C21[i] + C22[i] for i in range(m)])

def random_matrix(n):
    return [[random.randint(1, 9) for _ in range(n)] for _ in range(n)]

if __name__ == "__main__":
    print("Q1: Matrix Multiplication")
    print("Size | Traditional(s) | Strassen(s) | Match")
    for n in [2, 4, 8, 16, 32, 64]:
        A = random_matrix(n)
        B = random_matrix(n)

        t0 = time.perf_counter()
        C1 = traditional_multiply(A, B)
        t1 = time.perf_counter()

        t2 = time.perf_counter()
        C2 = strassen(A, B)
        t3 = time.perf_counter()

        print(f"{n:4} | {t1-t0:.6f}       | {t3-t2:.6f}   | {C1 == C2}")

        if n <= 4:
            print("A =", A)
            print("B =", B)
            print("Result =", C1)

# Analysis / Conclusion:
#The traditional matrix multiplication requires three nested loops, and hence its time is O(n3).
# complexity is O(n^3).
#Strassen breaks down each matrix into four parts, and applies 7 recursive
# multiplications instead of 8. Its recurrence is
# T(n) = 7T(n/2) + O(n^2), giving O(n^log2(7)) ≈ O(n^2.807).
#The two algorithms give the same answer. For small N, Strassen.Strassen (for small N).
#However, it may not be faster, due to the overhead involved in recursive calls and matrix-addition.
#The lower asymptotic complexity of its use may be beneficial for larger matrices.