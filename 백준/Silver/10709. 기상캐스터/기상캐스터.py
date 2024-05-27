H, W = map(int, input().split())
realAnswer = list()

for _ in range(H):
    cloud = list(map(str, input()))
    answer = list()
    
    count = -1
    for c in cloud:
        if c == 'c':
            answer.append(0)
            count = 0
        else:
            if count == -1:
                answer.append(-1)
            else:
                count += 1
                answer.append(count)
    realAnswer.append(answer)
    
for ans in realAnswer:
    print(*ans)