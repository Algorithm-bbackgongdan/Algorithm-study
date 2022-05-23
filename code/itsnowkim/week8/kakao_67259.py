from collections import deque

def solution(board):
    answer = 0
    size = len(board)
    road = [[999999999] * size for i in range(size)]
    
    # l, r, u, d is for
    # left, right, up, down
    # direction = [[0] * size for i in range(size)]
    movement = [[0,1,'r'],[0,-1,'l'],[1,0,'d'],[-1,0,'u']]
    
    # 초기화
    for i in range(0,size):
        if board[0][i] == 1:
            break
        else:
            road[0][i] = i
    
    for i in range(0,size):
        if board[i][0] == 1:
            break
        else:
            road[i][0] = i
    
    # 시작점 넣기
    visited = [[0] * size for i in range(size)]
    queue = deque()
    
    # 처음에는 오른쪽이나 아래 둘 중 하나로 무조건 이동함
    queue.append((0,0,'r'))
    queue.append((0,0,'d'))
    
    while queue:
        # queue에서 뽑고, 거기서 이동할 수 있는 지점을 queue에 넣는다.
        x,y,last_dir = queue.popleft()
        visited[x][y] = 1
        
        # 오른쪽, 왼쪽, 아래, 위 순서로 테스트
        for move in movement:
            new_x = x + move[0]
            new_y = y + move[1]
            new_dir = move[2]
            
            if 0 <= new_x < size and 0 <= new_y < size:
                # print(new_x,new_y,new_dir)
                # 보드 밖으로 안나감, 이동 가능한지부터 봄
                if board[new_x][new_y] != 1:
                    # 이전에 오던 방향과 같은 경우 추가비용없음
                    if last_dir == new_dir:
                        # 더 작다면 업데이트
                        if road[new_x][new_y] >= road[x][y] + 1:
                            road[new_x][new_y] = road[x][y] + 1
                            # direction[new_x][new_y] = new_dir
                            queue.append((new_x,new_y,new_dir))
                    # 이전에 오던 방향과 다른 경우 추가비용
                    else:
                        if road[x][y] + 6 <= road[new_x][new_y] + 2:
                            road[new_x][new_y] = road[x][y] + 6
                            # direction[new_x][new_y] = new_dir
                            queue.append((new_x,new_y,new_dir))
    
    return road[size-1][size-1] * 100
