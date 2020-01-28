def abbreviation(a, b):
    # built a zero matrix: (len(a)+1)*(len(b)+1)
    dp = [[0] * (len(b)+1) for i in range(len(a)+1)] 
    
    # first column: if the previous ones are all lower, then 1 
    dp[0][0] = 1
    stillLower = 1
    for i in range(1, len(a)+1):
        if stillLower == 1 and a[i-1].islower():
            dp[i][0] = 1
        elif a[i-1].isupper():
            stillLower = 0

    # for each column (b[j]):
    # - upper but not same: 0 // upper and same: look up *up-left*
    # - lower but not same: look *up* // upper and same: look *up-left* and *up*
    for j in range(1, len(b)+1): 
        for i in range(j, len(a)+1):
            if a[i-1].isupper():
                if a[i-1] == b[j-1]:
                    dp[i][j] = dp[i-1][j-1] # up-left
            else:
                if a[i-1].upper() == b[j-1]:
                    dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) # up-left or up
                else:
                    dp[i][j] = dp[i-1][j] # up
          
    return 'YES' if dp[-1][-1] == 1 else 'NO'
