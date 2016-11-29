# encoding=utf-8
import numpy as np
import scipy as sp
def make_A( Ad, vertex_num, edge_num):
    #make a sparse matrix
    size_number_list = [vertex_num,edge_num]
    A = np.zeros(size_number_list)
    l = -1
    #matlab里面是1-33 这里变成0-32问问老师
    for i in range(0,vertex_num-1):
        for j in range(i+1,vertex_num):
            if(Ad[i][j]) > 0.5:
                l = l + 1
                if(l == 78):
                    break
                A[i][l] = 1
                A[j][l] = -1
    return A
