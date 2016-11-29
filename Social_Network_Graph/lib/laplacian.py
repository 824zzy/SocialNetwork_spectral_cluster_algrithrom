# encoding=utf-8
# 求图的拉普拉斯矩阵 laplacian matrix of a graph
import numpy as np
def laplacian(A):
    #get size of A
    size_of_A = A.shape
    n = size_of_A[0]
    m = size_of_A[1]
    if( n != m):
        print "Matrix must be a square"
        return
    #transposed_A = np.transpose(A)
    #or_A = A|transposed_A
    d=(n,m)
    L = np.zeros(d)
    for i in range(0,n):
        for j in range(0,m):
            if(A[i][j] == A[j][i] and A[i][j] != 0):
                L[i][j] = -1
                L[j][i] = -1

    L = L - np.diag(sum(L))
    return L

