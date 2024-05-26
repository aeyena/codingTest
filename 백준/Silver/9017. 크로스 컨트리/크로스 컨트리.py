n = int(input())
for _ in range(n):
    m = int(input())
    tc = list(map(int, input().split()))
    
    teamN = max(tc)
    teamNArr = list()
    for i in range(1, teamN+1):
        count = 0
        for t in tc:
            if t == i:
                count += 1
        
        if count == 6:
            teamNArr.append(i)
            
    score = [0 for _ in range(m)]
    s = 0
    for i in range(m):
        if tc[i] in teamNArr:
            s += 1
            score[i] = s
            
    answer = [[] for _ in range(len(teamNArr))]
    for i in range(len(teamNArr)):
        for j in range(m):
            if tc[j] == teamNArr[i]:
                answer[i].append(score[j])
    
    mScore = 99999
    mIdx = 0
    for i in range(len(answer)):
        ms = 0
        for j in range(4):
            ms += answer[i][j]
            
        if mScore > ms:
            mIdx = i
            mScore = ms
        
        if mScore == ms:
            if answer[i][4] < answer[mIdx][4]:
                mIdx = i
                
    print(teamNArr[mIdx])