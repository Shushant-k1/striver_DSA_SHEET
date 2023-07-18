def subarraysXor(arr, x):
    n = len(arr)
    prefXor = {}
    ans = 0
    currXor = 0
    prefXor[0] = 1
    for i in range(n):
        currXor = currXor ^ arr[i]
        req = x ^ currXor
        if( req in prefXor):
            ans += prefXor[req]
        if(currXor in prefXor):        
            prefXor[currXor] = prefXor[currXor] + 1
        else: 
            prefXor[currXor] = 1
    return ans
