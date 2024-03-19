from collections import deque

# 두 개의 단어 차이 확인
def differCount(word1, word2):
    diff = 0
    for i in range(len(word1)):
        if (word1[i] != word2[i]):
            diff += 1
            if (diff > 1): return diff
    return diff
    

def solution(begin, target, words):
    visited = [0 for _ in range(len(words))] # 방문 확인
    dq = deque([(begin, 0)]) # (현재 단어, 변환 횟수)
    answer = 0

    while(dq):
        currentWord, step = dq.popleft()

        if currentWord == target:
            return step

        for i, word in enumerate(words):
            if visited[i] == 0 and differCount(currentWord, word) == 1:
                visited[i] = 1
                dq.append((word, step+1))
     
    return 0