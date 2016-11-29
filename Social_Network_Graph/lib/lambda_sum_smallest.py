# -*- encoding:utf-8 -*-
from lambda_sum_largest import  lambda_sum_largest

def lambda_sum_smallest( Y, k ):
    z= -lambda_sum_largest(-Y,k)
    return z