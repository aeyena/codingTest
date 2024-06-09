N = int(input())
answerList = [0] * (10**6 + 1)

answerList[2] = 1
answerList[3] = 1

if N==1:
    print(0)
elif N==2 or N==3:
    print(1)
else:
    for i in range(4, N+1):
        a, b, c = (10**6), (10**6), (10**6)
        if i%3 == 0:
            a = 1 + answerList[i//3]
        if i%2 == 0:
            b = 1 + answerList[i//2]
        c = 1 + answerList[i-1]
        answerList[i] = min(a,b,c)
    print(answerList[i])