N, score, P = map(int, input().split())

if N == 0:
    print(1)
else:
    scoreArr = list( map(int, input().split()) )
    
    if (N == P) and (min(scoreArr) >= score):
        print(-1)
    else:
        rank = 1
        for i in range(len(scoreArr)):
            if score < scoreArr[i]:
                rank += 1
                if i == (len(scoreArr)-1):
                    print(rank)
            else:
                print(rank)
                break