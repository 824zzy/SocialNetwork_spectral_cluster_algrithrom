# -*- encoding:utf-8 -*-
from sum_largest import sum_largest
# *args 表示可以传多个形式参数
# **kwargs 表示传的参数可以是字典
#foo(1,'b','c',a=1,b='b',c='c')
#args= (1, 'b', 'c')
#kwargs= {'a': 1, 'c': 'c', 'b': 'b'}

def sum_smallest( x, k, dim ):
    return - sum_largest( -x, k ,dim )