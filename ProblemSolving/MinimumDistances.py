#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumDistances function below.
def minimumDistances(a):
    hashMap = {}
    lis = []
    for i in range(len(a)):
        x = a[i]
        if(hashMap.get(x)!=None):
            lis.append(abs(hashMap.get(x)-i))
            hashMap[x]=i
        else :
            hashMap[x]=i
    if ( len(lis)!=0):
        return  min(lis)
    else:
        return -1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
