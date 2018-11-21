def matrixMulti(X,Y):
    n = len(X)
    Z = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                Z[i][j]+=X[i][k]*Y[k][j]
    return Z