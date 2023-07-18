from math import *
from collections import *
from sys import *
from os import *

def fourSum(arr, target):
    # Write your code here
    n = len(arr)
    arr.sort()
    d= dict()
    #print(arr)
    for i in range(n-1):
        for j in range(i+1,n):
            if (arr[i]+arr[j]) not in d:
                d[(arr[i]+arr[j])]=[(i,j)]
    for i in range(n-1):
        for j in range(i+1,n):
            if target-(arr[i]+arr[j]) in d:
                pairs = d[target-(arr[i]+arr[j])]
                for pair in pairs:
                    if pair[0] != i and pair[0] != j and pair[1] != i and pair[1] != j:
                        return "Yes"
    return "No"
