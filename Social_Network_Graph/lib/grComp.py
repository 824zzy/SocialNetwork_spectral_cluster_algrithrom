# -*- encoding:utf-8 -*-
from grValidation import grValidation
from grDecOrd import grDecOrd
import numpy as np
from grDecOrd import grDecOrd
def gr_comp(E, n):
    #取出grValidation的结果
    result_data = grValidation(E)
    m = result_data[0]
    n1 = result_data[1]
    E = result_data[2]
    #构造E2 第一列为E1的第一列和第二列；第二列为E1的第二列和第一列
    E_col1 = E[:,0].reshape(m,1)
    E_col2 = E[:,1].reshape(m,1)
    E2_sec1 = np.concatenate((E_col1, E_col2),axis=0)
    E2_sec2 = np.concatenate((E_col2, E_col1),axis=0)
    E2 = np.concatenate((E2_sec1,E2_sec2), axis=1)

    result_data2 = grDecOrd(E2)
    Dec = result_data2[0]
    Ord = result_data2[1]

    diag_list = []
    for each in range(Dec.shape[1]):
        diag_list.append(each+1)
    diag = np.diag(diag_list)
    temp = np.dot(Dec, diag)
    ncV = np.sum(temp , 1)
    transposed_ncV = np.transpose(ncV)
    return transposed_ncV
