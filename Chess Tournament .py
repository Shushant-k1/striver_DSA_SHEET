
def placed(dis,positions,c):        # we can fill rooms using that output
    c -= 1
    prev = positions[0]
    for i in range(1,len(positions)):
        if positions[i]-prev >= dis:
            c -= 1
            prev = positions[i]
        if c == 0:
            return True
    return False

def chessTournament(positions, n , c):
    positions.sort()
    low = 1
    high = positions[-1]-positions[0]
    res = 0
    while low<=high:          # binary search for options of output
        mid = (low+high)//2
        if placed(mid,positions,c):
            #res = mid 
            low = mid+1
        else:
            high = mid-1
    return low - 1
