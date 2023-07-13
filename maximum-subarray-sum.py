
def maxSubarraySum(arr, n) :

	# Your code here
    # return the answer
    s = 0
    ans = 0
    for i in range(n) :
        s += arr[i]
        ans = max(ans , s)
        if s < 0 :
            s = 0
    return ans
