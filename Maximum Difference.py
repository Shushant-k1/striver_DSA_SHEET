from typing import List
def maxDifference(n: int, arr: List[int]) -> int:
    # write yur code here
    arr.sort()
    ans = 0
    for i in range(n - 1) :
        ans  = max(ans , abs(arr[i] - arr[i + 1]))
    return ans
