# encoding=utf-8
import numpy as np
from laplacian import laplacian
#返回一个G|G'为拉普拉斯矩阵的第二小特征值
#k表示取第k小的特征值
#verbose打印一些信息的踪迹
#def fiedler(G,k,verbose):
def fiedler(G):
    #B为G的度矩阵
    B = sum(G)
    #D为度矩阵的全矩阵
    D = np.diag(B)
    #L是G的拉普拉斯矩阵
    L = laplacian(G)
    #求特征值D和特征向量V
    D,V = np.linalg.eig(L)
    #对特征值进行从小到大排序
    sorted_D = sorted(D)
    #取第二小特征值
    Lambda = sorted_D[1]
    #找特征值的位置
    k = 0
    for i in D:
        if(i == Lambda):
            break
        k = k + 1
    #去第二小特征值的特征向量
    eig_vector_list = []
    for each in V:
        eig_vector_list.append(each[k])
    return eig_vector_list




