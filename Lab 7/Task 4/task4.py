f1 = open('input4_2.txt','r')

n,x = map(int,f1().split())
cd = list(map(int,f1().split()))

def mc(cd,x):
    dp = [float('inf')]*(x+1)
    dp[0] = 0

    for coin in cd:
        for i in range(coin,x+1):
            dp[i] = min(dp[i],dp[i-coin]+1)
    return dp[x] if dp[x] != float('inf') else -1


result = mc(cd,x)
