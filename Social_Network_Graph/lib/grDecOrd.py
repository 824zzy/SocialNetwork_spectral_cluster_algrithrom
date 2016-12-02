# -*- encoding:utf-8 -*-
import numpy as np
from grValidation import grValidation
def grDecOrd(E):

    result_data = grValidation(E)
    n = result_data[1]
    E = result_data[2]
    #构造矩阵A ,但是构造不出来
    size_of_E = E.shape[0]
    A_size = (n,n)
    A = np.zeros(A_size)
    #把邻接的点的转换为列表
    E_ad_list = []
    E_ad =  (E[:,1]-1)*n + E[:,0]
    for i in range(size_of_E):
        E_ad_list.append(E_ad[i])
    for each in E_ad_list:
        raw_num = int(each / n)
        col_num = (each % n) - 1
        if(col_num == -1):
            raw_num = raw_num - 1
        A[raw_num][col_num] = 1
    # Ak是 n*n 的对角阵 ，As取的是Ak大于零的元素
    Ak = np.eye(n)
    As = Ak
    for k in range(n):
        Ak = np.dot(Ak,A)
        for i in range(0,n):
            for j in range(0,n):
                if Ak[i][j] != 0 or As[i][j] != 0 :
                    As[i][j] = 1
    #A额的矩阵是划分完社区的大矩阵
    A = As
    #ir是为一个两行的下标 python版本
    ir = np.unique(A, return_index=True)[1]
    T = np.arange(2*n).reshape(2,n)
    T[0,:] = A[ir[0],:]
    T[1,:] = A[ir[1],:]
    Dec = np.transpose(T)
    #构造Ord矩阵 2*2？？？
    Ord = np.arange(2*2).reshape(2,2)
    Ord[0][0] = A[ir[0],ir[0]]
    Ord[0][1] = A[ir[0],ir[1]]
    Ord[1][0] = A[ir[1],ir[0]]
    Ord[1][1] = A[ir[1],ir[1]]
    #获取分类的数量
    ns = Ord.shape[0]
    for it in range(ns * (ns-1) / 2):
        Mlow = np.tril(Ord, -1)
        none_zero_position = np.where(Mlow)
        if(none_zero_position == None):
            break
    #构造返回数据
    return_data = []
    return_data.append(Dec)
    return_data.append(Ord)
    return return_data