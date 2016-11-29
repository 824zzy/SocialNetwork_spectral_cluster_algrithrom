# -*- encoding:utf-8 -*-
import numpy as np
def grValidation(E):
    #取E的行数和列数
    siez_of_E = E.shape
    #m为行数
    m = siez_of_E[0]
    n = siez_of_E[1]

    #没有设置权重就都为1
    if(n < 3):
        add_colomn = np.arange(m).reshape(m,1)
        E = np.concatenate((E,add_colomn),axis=1)
        E[:, 2] = 1
    newE = E
    #找出E中前两列的最大值，也就是节点数
    max_list = []
    for each in newE[:,0]:
        max_list.append(each)
    for each in newE[:,1]:
        max_list.append(each)
    n = max(max_list)

    return_list = [m,n,newE]
    return  return_list

