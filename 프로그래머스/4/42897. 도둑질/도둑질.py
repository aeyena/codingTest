def solution(money):
    # 처음 숫자 제외
    dp1 = []
    dp1.append(0)
    dp1 += money[1:]
    
    # 마지막 숫자 제외
    dp2 = []
    dp2.append(0)
    dp2 += money[:-1]
    
    for i in range(2,len(money)):
        dp1[i] = max(dp1[i-1], dp1[i-2]+dp1[i])
        dp2[i] = max(dp2[i-1], dp2[i-2]+dp2[i])
        
    return max(dp1[-1],dp2[-1])
    