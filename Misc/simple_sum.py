
def maxDifference(px):
    # Write your code here
    print(px)
    #  edge cases
    if len(px) < 2: return -1
    
    # check for decreasing
    if sorted(px)[::-1] == px: return -1
    
    cur_max = 0
    for idx in range(len(px)-1, 0, -1):
        for runner in range(idx):
            print(f'{px[idx]}, {px[runner]}')
            diff = px[idx] - px[runner]
            if diff > 0:
                if diff > cur_max:
                    cur_max = diff
                    
    return cur_max
    
print(f'{maxDifference([7,1,2,5])}')