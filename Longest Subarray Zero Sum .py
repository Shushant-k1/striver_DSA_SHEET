from collections import Counter
def findDuplicate(arr, n):
   counter = Counter(arr)
   for num, count in counter.items():
       if count > 1:
           return num
   return -1  
