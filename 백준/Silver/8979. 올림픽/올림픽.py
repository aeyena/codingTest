N, K = map(int, input().split())
medals = list()
for _ in range(N):
    arr = tuple(map(int, input().split()))
    medals.append(arr)

rank = [0 for _ in range(N+1)]

medals.sort(key=lambda x:(x[1], x[2], x[3]), reverse=True)

idx = [medals[i][0] for i in range(N)].index(K)

for i in range(N):
    if medals[idx][1:] == medals[i][1:]:
        answer = i+1
        break

print(answer)