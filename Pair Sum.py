def pairSum(arr, s):
    # Write your code here.
    # arr.sort()
    mp = {}
    ans = []
    for i in range(len(arr)):
        ele = arr[i]
        t = s - ele
        if t in mp:
            lst = [min(ele, t), max(ele,t)]
            for i in range(mp[t]):
                ans.append(lst)
        mp[ele] = mp.get(ele, 0) + 1
    ans.sort()
    return ans
