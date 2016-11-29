# encoding=utf-8
import numpy as np
def newmatrix(Distance, A, edge_num, B, Pos):
    #把Pos位置的B中信息删除
    B[int(Distance[Pos-1][0]) - 1] = B[int(Distance[Pos-1][0]) - 1] - 1
    B[int(Distance[Pos-1][1]) - 1] = B[int(Distance[Pos-1][1]) - 1] - 1
    shape_A = A.shape
    colomn = shape_A[1]
    #把Pos位置的A中信息删除
    colomn_index_list = []
    A1 = A[:,0:Pos - 1]
    A2 = A[:,Pos:colomn]
    A = np.concatenate((A1,A2),axis=1)
    edge_num2 = edge_num - 1
    result_list = []
    result_list.append(A)
    result_list.append(edge_num2)
    result_list.append(B)
    return result_list
