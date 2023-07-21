def removeDuplicates(arr,n):
    # Write your code here.
    ans  = 0
    for i in range( n - 1) :
        if arr[i] == arr[i +1] :
            continue
        else :
            ans += 1
    return ans +1
