# encoding=utf-8
import numpy as np
def make_al(vertex_num, index1, index2):
    al_size=(vertex_num,1)
    al = np.zeros(al_size)
    for j in range(0,vertex_num):
        if(j == index1 - 1):
            al[j] = 1
        elif(j == index2 - 1):
            al[j] = -1
        else:
            al[j] = 0
    return al
