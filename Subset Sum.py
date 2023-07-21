def subsetSum(num: List[int]) -> List[int]:
    # Write your code here.
    z = [0]
    for i in range(1 , 2 ** len(num)): 
        x = list(bin(i))
        x = x[2:]
        x = x[::-1]
        count = 0
        for i in range( len(x)) :
            if x[i] == "1" :
                count += num[i]
        z.append(count)
    z.sort()
    return z
