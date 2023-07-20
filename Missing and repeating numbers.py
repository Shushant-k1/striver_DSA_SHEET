from math import *
from collections import *
from sys import *
from os import *

def missingAndRepeating(arr, n):
    m=None
    r=None
    for i in range(1,n+1):
        if i not in arr:
            m=i
            break
    for i in range(n):
       for j in range(i+1,n):
           if arr[i]==arr[j]:
               r=arr[i]
               break
    return m,r
