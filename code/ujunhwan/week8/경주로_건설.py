import heapq

def solution(board):
    # 건설 비용을 계산해 보니 직선 도로 하나를 만들 때는 100원이 소요되며, 코너를 하나 만들 때는 500원이 추가로 듭니다.
    
    # 동 남 서 북
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    
    N = len(board[0])
    
    def is_valid(y, x):
        return 0 <= y < N and 0 <= x < N
    
    # pos, cost, direction
    q = []
    
    dist = [[float('inf') for col in range(4)] for row in range(N*N)]
    for i in range(4):
        dist[0][i] = 0
        heapq.heappush(q, ([0, 0, i]))
    
    while q:
        pos, cost, direction = heapq.heappop(q)
        y, x = pos//N, pos%N
        
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            npos = ny*N+nx
            ncost = cost + 100 if direction == k else cost + 600
            if is_valid(ny, nx) and board[ny][nx] == 0:
                if dist[npos][k] > ncost:
                    dist[npos][k] = ncost
                    heapq.heappush(q, [npos, ncost, k])
    '''
    for i in range(N):
        print(dist[i*N:i*N+N])
    '''
        
    answer = min(dist[N*N-1])
    return answer