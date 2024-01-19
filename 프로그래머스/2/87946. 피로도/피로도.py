from itertools import permutations 
def solution(k, dungeons):
    max_num = len(dungeons) 
    answer = 0
    for pairs in permutations(dungeons,max_num): #가능한 순서 배열 추출(2차원배열)
        kCopy = k 
        count = 0
        for pair in pairs: 
            if kCopy<pair[0]: 
                break
            kCopy -= pair[1]
            count += 1
        if count == max_num : #답으로 가능한 최대수
            return count
        if count>answer: 
            answer = count
    return answer