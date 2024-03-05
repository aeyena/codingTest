INF = 987654321

def solution(arr):
    nums,ops = [], []
    for idx, element in enumerate(arr):
        nums.append(element) if not idx % 2 else ops.append(element)

    N = len(nums)
    # dp_max[i][j] = i번째부터 j번째까지 구간의 연산의 최댓값
    dp_max = [[-INF] * N for _ in range(N)] 
    # dp_min[i][j] = i번째부터 j번째까지 구간의 연산의 최솟값
    dp_min = [[INF] * N for _ in range(N)] 

    for scope in range(N): #i와 j의 간격
        for start in range(N-scope): #i부터 j까지의 연산을 수행함
            end = start + scope

            if scope == 0:
                dp_max[start][start] = dp_min[start][start] = int(nums[start])
                continue

            for mid in range(start, end): #i부터 j까지 돌면서, 괄호를 하나는 늘리고, 하나는 줄여서 각각의 범위 연산을 수행함
                if ops[mid] == '+': # mid번째에 해당되는 연산이 + 일 경우
                    dp_max[start][end] = max(dp_max[start][mid] + dp_max[mid+1][end], dp_max[start][end]) # +일 경우 최댓값은 최댓값 + 최댓값임
                    dp_min[start][end] = min(dp_min[start][mid] + dp_min[mid+1][end], dp_min[start][end]) # +일 경우 최솟값은 최솟값 + 최솟값임
                else: # mid번째에 해당되는 연산이 - 일 경우
                    dp_max[start][end] = max(dp_max[start][mid] - dp_min[mid+1][end], dp_max[start][end]) # -일 경우 최댓값은 최댓값 - 최솟값임
                    dp_min[start][end] = min(dp_min[start][mid] - dp_max[mid+1][end], dp_min[start][end]) # -일 경우 최솟값은 최솟값 - 최댓값임
        
    return dp_max[0][-1]