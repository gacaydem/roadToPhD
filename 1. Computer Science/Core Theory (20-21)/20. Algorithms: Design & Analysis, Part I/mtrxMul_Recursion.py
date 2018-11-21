def split2pwrMatrix(X):
    n = len(X)
    A = [[X[i][j] for j in range(n//2)] for i in range(n//2)]
    B = [[X[i][j] for j in range(n//2,n)] for i in range(n//2)]
    C = [[X[i][j] for j in range(n//2)] for i in range(n//2,n)]
    D = [[X[i][j] for j in range(n//2,n)] for i in range(n//2,n)]
    return A,B,C,D

def matrixSummarize(X,Y):
    n = len(X)
    Z = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            Z[i][j] = X[i][j]+Y[i][j]
    return Z

def matrixConcanate(X,Y,U,V):
    n = len(X)
    Z = [[0 for j in range(n*2)] for i in range(n*2)]
    for i in range(n):
        for j in range(n):
            Z[i][j] = X[i][j]
    for i in range(n):
        for j in range(n,n*2):
            Z[i][j] = Y[i][j-n]
    for i in range(n,n*2):
        for j in range(n):
            Z[i][j] = U[i-n][j]
    for i in range(n,n*2):
        for j in range(n,n*2):
            Z[i][j] = V[i-n][j-n]
    
    return Z

def recMatrixMulti(X,Y):
    n = len(X)
    Z = [[0 for j in range(n)] for i in range(n)]
    if n<2:
        return [[X[0][0]*Y[0][0]]]
    else:
        A,B,C,D = split2pwrMatrix(X)
        E,F,G,H = split2pwrMatrix(Y)
        AE = recMatrixMulti(A,E)
        BG = recMatrixMulti(B,G)
        AF = recMatrixMulti(A,F)
        BH = recMatrixMulti(B,H)
        CE = recMatrixMulti(C,E)
        DG = recMatrixMulti(D,G)
        CF = recMatrixMulti(C,F)
        DH = recMatrixMulti(D,H)
        
        Z1 = matrixSummarize(AE,BG)
        Z2 = matrixSummarize(AF,BH)
        Z3 = matrixSummarize(CE,DG)
        Z4 = matrixSummarize(CF,DH)
        matrix = matrixConcanate(Z1,Z2,Z3,Z4)
        
    return matrix

X = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
Y = [[5,6,7,8],[6,7,8,9],[7,8,9,10],[8,9,10,11]]

print(recMatrixMulti(X,Y))