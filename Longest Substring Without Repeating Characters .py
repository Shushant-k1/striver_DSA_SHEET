def uniqueSubstrings(st) :
    # Write your code here
    d = {}
    start = 0
    ans = 0
    for i in range(len(st)):
        if st[i] in d and start <= d[st[i]]:
            start = d[st[i]] + 1
        else : 
            ans = max(ans , i + 1 - start)
        d[st[i]] = i
    return ans
