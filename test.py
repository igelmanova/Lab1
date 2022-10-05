A = [1,3,45,23,66,101,582]
x_max, x_min = max(A), min(A)
for i in range(len(A)):
    if A[i] % 2 == 0:
        A[i] = A[i] * x_min 
    else:
        A[i] = A[i] * x_max
print(A)