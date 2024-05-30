# Ordenar en forma creciente tres valores diferentes A, B, C.
import random
A = random.randrange(1,10)
B = random.randrange(1,10)
C = random.randrange(1,10)

print(A,B,C)

if (A != B != C != A): 
    if (A < B < C):
        print(A, B, C)
    elif (A < C < B):
        print(A, C, B)
    elif (B < A < C):
        print(B, A, C,)
    elif (B < C < A):
        print(B, C, A)
    elif (C < A < B):
        print(C, A, B)
    elif (C < B < A):
        print(C, B, A)
else:
    print("Hay valores que son iguales")
