def longestSubSeg(arr, n, k):
    #   Write your code here.
    mx = 0
    l = 0
    count = 0
    for i in range(n) :
        if arr[i] == 0 :
            count += 1
        while count > k :
            if arr[l] == 0 :
                count -= 1
            l += 1
        mx = max(mx , i - l + 1)
    return mx
