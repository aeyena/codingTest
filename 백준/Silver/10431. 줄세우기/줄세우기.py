p = int(input())
answer = list()
for _ in range(p):
    N, *arr = map(int, input().split())
    cnt = 0
    for i in range(20):
        m = arr[i]
        for j in range(i-1,-1,-1):
            if m < arr[j]:
                arr.remove(m)
                arr.insert(j, m)
                cnt += 1
    answer.append([N, cnt])

for ans in answer:
    print(*ans)