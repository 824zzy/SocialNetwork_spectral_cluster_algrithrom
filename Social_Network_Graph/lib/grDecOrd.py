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
    # Ak是 n*n 的对角阵 ，As取的事Ak大于零的元素，（这两个不就一样么？？？？？？？？？？？）
    Ak = np.eye(n)
    As = Ak
    for i in range(n):

    print Ak
    return