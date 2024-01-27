from collections import deque
def solution(n, wires):
    m = 999999999999 #송전탑 개수의 차이
    for [a,b] in wires: 
        wiresCopy = deque(wires)
        isA = {a} #하나의 전력망이 가지고 있는 송전탑 번호들이 담긴 set
        isB = {b}
        while(wiresCopy):
            if wiresCopy[0]==[a,b]: 
                wiresCopy.popleft()
                continue
            if wiresCopy[0][0] in isA:
                isA.add(wiresCopy.popleft()[1])
                continue
            if wiresCopy[0][1] in isA:
                isA.add(wiresCopy.popleft()[0]) 
                continue
            if wiresCopy[0][0] in isB:
                isB.add(wiresCopy.popleft()[1])
                continue
            if wiresCopy[0][1] in isB:
                isB.add(wiresCopy.popleft()[0])
                continue
            wiresCopy.append(wiresCopy.popleft())
        if abs(len(isA)-len(isB))<m:
            m = abs(len(isA)-len(isB))
    return m