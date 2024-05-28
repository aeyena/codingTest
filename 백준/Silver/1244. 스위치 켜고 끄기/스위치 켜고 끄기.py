switchN = int(input())
switch = list(map(int, input().split()))
studentN = int(input())

for _ in range(studentN):
    sex, num = map(int, input().split())
    
    if sex == 1:
        for i in range(num-1, switchN, num):
            if switch[i] == 1:
                switch[i] = 0
            else:
                switch[i] = 1
    else:
        interval = min(num-1, switchN-num)
        idx = num-1

        for i in range(1, interval+1):
            if switch[idx+i] == switch[idx-i]:
                if switch[idx+i] == 1:
                    switch[idx+i] = 0
                    switch[idx-i] = 0
                else:
                    switch[idx+i] = 1
                    switch[idx-i] = 1
            else:
                break
        
        if switch[idx] == 1:
            switch[idx] = 0
        else:
            switch[idx] = 1

for i in range(switchN):
    print(switch[i], end=" ")
    if (i+1) % 20 == 0:
        print()