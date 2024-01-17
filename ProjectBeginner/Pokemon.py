powers = [1, 12, 4, 9]

mini,maxi = 0, 0

def minFct(min,val):
    if(min > val):
        return val
    return min

def maxFct(max,val):
    if(max < val):
        return val
    return max

for power in powers:
    if mini == 0 and maxi == 0:
        mini,maxi = power,power
        print(mini,maxi)
    else:
        mini = minFct(mini,power)
        maxi = maxFct(maxi,power)
        print(mini,maxi)
