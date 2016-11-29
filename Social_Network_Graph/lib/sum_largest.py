# -*- encoding:utf-8 -*-
import numpy as np
import math
# return sum of the largest k values of a vector

#sum()传的参数可以是一个列表或者数组，方便得很
#dim默认为1
def sum_largest( x, k, dim ):
    x_list = []
    for each in x:
        x_list.append(each)
    #determin output size
    sx = 1
    nd = max(dim,sx)
    ones = np.ones(dim - nd + 1)
    list_ones = list(ones)
    sx = np.array(list_ones)
    sy = sx
    #compute result
    if k < 0:
        return np.zeros(sy)
    elif k <= 1:
        max_val_num = [ k * max (x) ]
        max_val = np.array(max_val_num)
        return max_val
    elif k >= len(x):
        return sum(x)
    else:
        max_list=[]
        x_list.sort(reverse = True)
        for each in range(k):
            max_list.append(x_list[each])
        max_val = np.array(max_list)
        result = 0
        for each in max_val:
            result = result + each
        return result





#test
#a=sum_smallest([1,2,3,6,5,4],3,1)