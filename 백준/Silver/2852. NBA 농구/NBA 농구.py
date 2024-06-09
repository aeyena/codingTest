N = int(input())

score1 = 0
score2 = 0
time1 = 0
time2 = 0
preTime = 0

for _ in range(N):
    num, time = input().split()
    time = int(time[:2]) * 60 + int(time[3:])
    
    if score1 > score2:
        time1 += (time - preTime)
    elif score1 < score2:
        time2 += (time - preTime)
    
    if num == "1":
        score1 += 1
    else:
        score2 += 1
        
    preTime = time

if score1 > score2:
    time1 += (48 * 60 - preTime)
elif score1 < score2:
    time2 += (48 * 60 - preTime)
    
print("%02d:%02d" %(time1 // 60, time1 % 60))
print("%02d:%02d" %(time2 // 60, time2 % 60))