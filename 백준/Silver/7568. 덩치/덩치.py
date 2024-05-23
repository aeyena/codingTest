N = int(input())
people = list()
for i in range(N):
    arr = list(map(int, input().split()))
    arr.append(i)
    people.append(arr)

people.sort(key=lambda x:(x[0], x[1]), reverse=True)

answer = [0 for _ in range(N)]

for i in range(N):
    
    rank = 1
    
    for j in range(i):
        if (people[i][0] < people[j][0]) and (people[i][1] < people[j][1]):
            rank += 1
            
    answer[people[i][2]] = rank 

print(*answer)