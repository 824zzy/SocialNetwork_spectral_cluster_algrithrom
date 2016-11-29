# encoding=utf-8
#G为连接矩阵，将G划分为G1和G2两个社区
#G1,G2与G规格相同
import numpy as np
def Divide2(G,node_G,ncV):
    #将G的对角线初始化为0
    G = G - np.diag(G)
    #G中节点数
    size_of_G = G.shape
    Number = size_of_G[0]
    #求G中的非零元素的并集
    index_list = []
    np.argwhere()
    for each in np.sum(G,axis=0):

        index_list.append()
    if( np.sum(G,axis=0) != 0):
        index_list.append()
    NonNumber = union
    #求G中非零元素的交际



G = np.random.rand(10.10)
Divide2(G,10,10)