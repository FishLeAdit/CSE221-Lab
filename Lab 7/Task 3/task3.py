f1 = open('input3_4','r')
a = f1.readlines()
n = int(a)

def ccs(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3,n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp(n)

result = ccs(n)
f2 = open('output3_4','w')
f2.write(result)