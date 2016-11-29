# encoding=utf-8
import numpy as np


#reflectArr为两行34列 和 matlab中的34列两行不一样，第一行是序号，第二行是数据

def read_Graph(wholemap, communities):

    with open(wholemap,'r') as f:
        data_list_wholemap = []
        for each in f.readlines():
            line=each.strip()
            List=line.split(' ')
            data_list_wholemap.append(List)
        vertex_num = data_list_wholemap[0]
        edge_num = data_list_wholemap[1]



    with open(communities,'r') as f:
        data_list_communities = []
        for each in f.readlines():
            line=each.strip()
            List=line.split(' ')
            data_list_communities.append(List)

        data_temp = data_list_communities[0]
        reflectArr_list1=[]
        reflectArr_list2=[]
        for each in range(int(vertex_num[0])):
            reflectArr_list1.append(each + 1)
        for each in data_temp:
            reflectArr_list2.append(int(each))

        reflectArr1 = np.array(reflectArr_list1)
        reflectArr2 = np.array(reflectArr_list2)
        sizeof_reflectArr = reflectArr1.shape
        colomn_number = sizeof_reflectArr[0]
        reflectArr_temp = np.concatenate((reflectArr1,reflectArr2))
        reflectArr=reflectArr_temp.reshape(2,colomn_number)

    i=0
    sizeof_Ad = int(vertex_num[0])
    Ad = np.zeros(sizeof_Ad*sizeof_Ad).reshape(sizeof_Ad,sizeof_Ad)
    with open(wholemap,'r') as f:
        for each in f.readlines():
            line=each.strip()
            List=line.split(' ')
            i=i+1
            if(i>2):
                Ad[int(List[0]) - 1] [int(List[1]) - 1]= 1

    result_list=[Ad,vertex_num,edge_num,reflectArr]
    return result_list

