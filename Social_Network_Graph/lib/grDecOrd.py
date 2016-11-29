# -*- encoding:utf-8 -*-
import numpy as np
from grValidation import grValidation
def grDecOrd(E):

    result_data = grValidation(E)
    print E
    n = result_data[1]
    E = result_data[2]
    # #构造矩阵A ,但是构造不出来
    # A_size = (n,n)
    # A = np.zeros(A_size)
    # temp1 = (E[:,1] - 1) * n
    # temp2 = E[:,0]
    # temp  = temp1 + temp2
    # A[temp] = 1!!!!!!!!!!!!!!1
    #A[E[:,1]-1]
    #Ak是 n*n 的对角阵 ，As取的事Ak大于零的元素，（这两个不就一样么？？？？？？？？？？？）
    Ak = np.eye(n)
    As = Ak
    return