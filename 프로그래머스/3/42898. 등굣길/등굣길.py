def solution(m, n, puddles):
    # 모든 칸의 최단 경로 수 1로 초기화
    path = [[1 for i in range(m)] for _ in range(n)]

    # 물웅덩이가 있는 칸의 최단 경로 수를 0으로 변경
    for puddle in puddles:
        path[puddle[1]-1][puddle[0]-1] = 0
        # 1행에 물웅덩이가 있으면 그 이후 오른쪽칸들의 최단 경로 수는 0
        if puddle[1] == 1:
            for i in range(puddle[0],m):
                path[0][i] = 0
        # 1열에 물웅덩이가 있으면 그 이후 아래칸들의 최단 경로 수는 0
        if puddle[0] == 1:
            for i in range(puddle[1],n):
                path[i][0] = 0

    # 각 칸의 최단 경로 수 구하기
    for i in range(n-1):
        for j in range(m-1):
            # 물웅덩이는 계산하지 않고 넘어가기
            if(path[i+1][j+1] == 0):
                continue
            path[i+1][j+1] = path[i][j+1] + path[i+1][j]

    return path[-1][-1] % 1000000007