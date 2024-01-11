from itertools import permutations

def solution(numbers):
    answer = 0
    perList = list()
    for i in range(len(list(map(int,str(numbers))))):
        for num in permutations(numbers,i+1): #조합할 수 있는 모든 숫자쌍 추출
            isPrime = int(''.join(map(str,num))) #숫자쌍을 숫자로 변환
            if isPrime in perList:
                continue
            else:
                perList.append(isPrime)
                if isPrime==2: answer+=1 
                for j in range(2,isPrime): #소수 판별
                    if isPrime % j == 0:
                        break
                    if j==(isPrime-1):
                        answer +=1       
    return answer  