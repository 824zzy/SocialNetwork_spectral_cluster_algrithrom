# encoding=utf-8
__author__ = '朱正源'
import numpy as np
from lib.calculate_time import tic
from lib.calculate_time import toc
from lib.read_data import read_data
from mainFunctionD2 import mainFunctionD2
from lib.read_Graph import read_Graph
import networkx as nx
import matplotlib.pyplot as plt

#读取数据wholemap
data_karateresult = 'new_comOne'
wholeMap = read_data( data_karateresult )

#读取数据 communities
data_karatecommunity = 'community'
communities = read_data( data_karatecommunity )

#开始计算程序消耗的时间?????!!!!时间计算有问题！
tic()

#读取图 Read the Graph
Graph_Message = []
Graph_Message = read_Graph(wholeMap,communities)
Ad = Graph_Message[0]

vertex_num_list = Graph_Message[1]
vertex_num = int(vertex_num_list[0])

edge_num_list = Graph_Message[2]
edge_num = int(edge_num_list[0])

reflectArr_list = Graph_Message[3]
reflectArr = reflectArr_list[0]



#初始化node_G To initialize Node_G
#node_G 为 一行34列的 矩阵
int_vertex_num = int(vertex_num)
nodes_G = np.arange(1,int_vertex_num+1)
# #调用mainFuntion_D2
mainFunctionD2( Ad, vertex_num, edge_num, nodes_G, 1, 0)
#
# #显示计算程序消耗的时间
# toc()
