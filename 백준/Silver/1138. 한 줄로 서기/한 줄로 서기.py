n = int(input())
answer = [0]*n
arr = [int(h) for h in input().split()]

for i in range(n):
    total = 0
    for j in range(n):
        if answer[j] == 0:
            if total == arr[i]:
                answer[j] = i+1 
            total += 1

for ans in answer:
    print(ans, end=" ")