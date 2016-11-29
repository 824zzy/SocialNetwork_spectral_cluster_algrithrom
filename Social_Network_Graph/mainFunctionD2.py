# encoding=utf-8
from lib.calculate_time import tic,toc
import scipy as sp
import numpy as np
from lib.make_A import make_A
from lib.make_distance import make_distance
from lib.lambda_sum_smallest import lambda_sum_smallest
from lib.fiedler import fiedler
from lib.make_al import make_al
import math
from lib.newmatrix import newmatrix
from lib.grComp import gr_comp
from lib.Divide2 import Divide2

def mainFunctionD2( Ad, vertex_num, edge_num, nodes_G, iter_times, group):
    s = []
    s.append(vertex_num)
    if (vertex_num == 3 or edge_num < 5 or iter_times > 4 ):
        print "something strange in mainfuntiond2"
        return
    iter=1
    tic()
    #the transposed matrix of Adjacent matrix
    #邻接矩阵补全下三角！
    size_of_Ad = Ad.shape
    transposed_Ad = np.transpose(Ad)
    for i in range(size_of_Ad[0]):
        for j in range(size_of_Ad[1]):
            Ad[i][j] = Ad[i][j] or transposed_Ad[i][j]
    #得出A 有1和-1的34行78列的矩阵
    A = make_A(Ad, vertex_num, edge_num)
    transposed_A = np.transpose(A)
    #列求和得出度矩阵B 34行一列 看成一个列表就行
    B = sum(Ad)
    #构造一个78*5的距离矩阵
    Distance = make_distance(Ad, A, vertex_num, edge_num, B)
    #变量POS记录Distance中第五行中最大值所在的位置
    max_list = []
    for each in Distance[:,4]:
        max_list.append(each)
    Pos = max_list.index(max(max_list)) + 1
    #把度矩阵展开成全矩阵,并且构造拉普拉斯矩阵
    D = np.diag(B)
    L = np.dot(A, transposed_A)
    W = Ad
    L1 = D - W
    cutIndexSign = 0
    #构造x为L的升序特征值矩阵
    eig_val,eig_vec = np.linalg.eig(L)
    eig_val_list = []
    for each in eig_val:
        eig_val_list.append(each)
    eig_val_list = sorted(eig_val_list)
    x = np.array(eig_val_list)
    x = np.diag(x)
    #构造Q得L的正交规范化矩阵（求矩阵正交基）
    Q = sp.linalg.orth(L)
    #求L的费德勒向量：第二小特征值的特征向量
    v = fiedler(L)
    #找特征向量的特征值
    lambda2 = lambda_sum_smallest(L,2)
    print "ECCEM"
    print "切割第"+str(iter)+"次"
    #t为算法运行的时间，写入time中
    t=toc()
    with open("/home/a/PycharmProjects/TestZhu/tjufe_1/Social_Network_Graph/output_data/time.txt","a") as f:
        f.write(str(t)+"\n")
        f.close()
    #求第三小的lambda
    lambda3 = lambda_sum_smallest(L,3)-lambda2
    aa = (v[int(Distance[Pos - 1][0])-1] - v[int(Distance[Pos - 1][1])-1]) ** 2

    b1 = 1 + (2 - aa) / (lambda2 - lambda3)
    low = lambda2 - aa / b1
    #矩阵U是Q的转置和al的积
    al = make_al(vertex_num,Distance[Pos-1][0],Distance[Pos-1][1])
    transposed_Q = np.transpose(Q)
    u = np.dot(transposed_Q,al)
    with open("/home/a/PycharmProjects/TestZhu/tjufe_1/Social_Network_Graph/output_data/out.txt","a") as f:
        f.write(str(lambda2)+"\n")
        f.close()

    while(lambda2>math.exp(-23)):
            cutIndexSigen = 1
            if( vertex_num == 1 or edge_num < 3):
                break
            #将矩阵中的信息A,edge_num,B进行刷新

            result_list = newmatrix(Distance, A, edge_num, B, Pos)
            A = result_list[0]
            edge_num = result_list[1]
            B = result_list[2]
            Distance = make_distance(Ad, A, vertex_num, edge_num, B)
            max_list = []
            for each in Distance[:,4]:
                max_list.append(each)
            Pos = max_list.index(max(max_list)) + 1
            iter = iter + 1
            print "切割第" + str(iter) + "次"
            D = np.diag(B)
            transposed_A = np.transpose(A)
            L = np.dot(A, transposed_A)
            v = fiedler(L)

            #有结点取为零直接跳出循环
            list_B = []
            for each in B:
                list_B.append(each)
            if(0 in list_B):
                print "Distance_size[0]有节点度为0的孤立节点跳出了循环"
                break
            lambda2 = lambda_sum_smallest(L, 2)
            #写一次时间
            t=toc()

            with open("/home/a/PycharmProjects/TestZhu/tjufe_1/Social_Network_Graph/output_data/time.txt","a") as f:
                f.write(str(t) + "\n")
                f.close()
            lambda3 = lambda_sum_smallest(L,3)-lambda2
            a1 = (v[int(Distance[Pos - 1][0])-1] - v[int(Distance[Pos - 1][1])-1]) ** 2
            b1 = 1 + (2 - a1) / (lambda2 - lambda3)
            low = lambda2 - a1 / b1
            with open("/home/a/PycharmProjects/TestZhu/tjufe_1/Social_Network_Graph/output_data/out.txt","a") as f:
                f.write(str(lambda2) + "\n")
                f.close()
    #构造comMatrix 就是Distance的前两行
    Distance_size = Distance.shape
    compMatrix = np.arange(Distance_size[0]*2).reshape(Distance_size[0],2)
    i = 0
    for each in Distance[:,0]:
        compMatrix[i][0] = each
        i = i + 1
    j = 0
    for each in Distance[:,1]:
        compMatrix[j][1] = each
        j = j + 1
    ncV = gr_comp(compMatrix,vertex_num)
    s.append(group)
    s.append(iter_times)
    with open("/home/a/PycharmProjects/TestZhu/tjufe_1/Social_Network_Graph/output_group/out.txt","a") as f:
        f.write(str(s)+"\n")
        f.closed
    nodes_G = np.transpose(nodes_G)








    result_list_of_Divide2 = D











