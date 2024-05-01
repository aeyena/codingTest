a, b, c = map(int, input().split())
truck = []
min_s1 = 100
max_s2 = 0
for i in range(3):
    s_arr = []
    s1, s2 = map(int, input().split())
    if s1 < min_s1:
        min_s1 = s1
    if s2 > max_s2:
        max_s2 = s2
    s_arr.append(s1)
    s_arr.append(s2)
    truck.append(s_arr)
    
answer = 0


for i in range(min_s1, max_s2):
    cnt = 0
    for s_arr in truck:
        # 주차장에 주차된 트럭 수 세기
        if s_arr[0] <= i and s_arr[1] > i:
            cnt += 1
    
    if cnt == 1:
        answer += a
    elif cnt == 2:
        answer += b * 2
    elif cnt == 3:
        answer += c * 3
        
print(answer)