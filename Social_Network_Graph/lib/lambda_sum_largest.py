# -*- encoding:utf-8 -*-
from sum_largest import  sum_largest
import numpy as np
from numpy import linalg as LA

#the sum of the k largest eigenvalues of a symmetric matrix
# float("inf") 表示无穷大


def lambda_sum_largest(Y, k):
    #判断是否为对阵矩阵 To determine whether a symmetric matrix or not
    if(Y.shape[0] != Y.shape[1]):
        print "First input must be a square matrix"
    #取Y的特征值直接进sum_largest函数
    eig_value,eig_vetor = np.linalg.eig(Y)
    z=sum_largest(eig_value,k,1)
    return z
