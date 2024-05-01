def solution(n, times):
    left = 1
    # 가장 긴 심사시간이 소요되는 심사관에게 n명 모두 심사받는 경우 
    # 가장 비효율적으로 심사했을 때 걸리는 시간
    right = max(times)*n 
    
    while(left <= right):
        total = 0
        mid = (left + right) // 2
        
        for time in times:
            # 모든 심사관들이 mid분 동안 심사한 사람의 수
            total += mid // time
            if(total >= n):
                break
            
        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 많거나 같은 경우
        if n <= total:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer