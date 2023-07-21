from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def calculateMinPatforms(at, dt, n):
    # Write your code here.
    z = []
    for i in range(n) :
        z.append(["A" , at[i]])
        z.append(["B" , dt[i]])
    z.sort(key = lambda x : x[0])
    z.sort(key = lambda x: x[1])
    ans = 0
    count = 0
    for i in range(len(z)) :
        if z[i][0] =="A" :
            count += 1
        else :
            count -= 1
        ans = max(ans, count)
    return ans
