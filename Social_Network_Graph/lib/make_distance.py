#  encoding=utf-8
import numpy as np
from fiedler import fiedler
import math
from scipy.sparse import coo_matrix, vstack
#B为对角阵；
def make_distance(Ad,A,vertex_num,edge_num,B):

    #把B转换为对角阵再转换为全矩阵
    D= np.diag(B)
    #Y_transposed为Y的转置矩阵
    A_transposed = np.transpose(A)
    #L2为A和A的转职的积
    L2 = np.dot(A,A_transposed)
    #求L2的费德勒向量
    v = fiedler(L2)
    #构建距离矩阵初始化为空
    size_of_distance_matrix = (edge_num,5)
    Distance = np.zeros(size_of_distance_matrix)
    index1 = 0
    index2 = 0
    count = 0

    for i in range(0,edge_num):
        for j in range(0,vertex_num):
            if(A[j][i] == 1):
                index1 = j
            elif(A[j][i] == -1):
                index2 = j
                break
        Distance[count][0] = index1+1
        Distance[count][1] = index2+1
        Distance[count][2] = i+1
        Distance[count][3] = 0
        if(B[index1] == 1 or B[index2] == 1):
            Distance[count][4] = 1/math.exp(100)
        else:
            w = 1/math.exp(max((abs(v[index1]), abs(v[index2]))))
            Distance[count][4]=w*((v[index1]-v[index2])**2)
        count = count + 1
    return Distance