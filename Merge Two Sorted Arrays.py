from math import *
from collections import *
from sys import *
from os import *

def ninjaAndSortedArrays(arr1,arr2,m,n):
    # Write your code here.
    i , j = 0 , 0
    z = []
    while i < m and j < n :
        if arr1[i] <=arr2[j] :
            z.append(arr1[i])
            i += 1
        else :
            z.append(arr2[j])
            j += 1
    while i < m :
        z.append(arr1[i])
        i += 1
    while j < n :
        z.append(arr2[j])
        j += 1
    return z
