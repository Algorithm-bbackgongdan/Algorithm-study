from collections import deque


def solution(board):
    N = len(board)

    costmap = [[987654321 for _ in range(N)] for __ in range(N)]
    costmap[0][0] = 0
    q = deque()

    q.append((0, 0, 0, 0))
    q.append((0, 0, 0, 3))

    while q:
        x, y, cost, drc = q.popleft()

        for dx, dy, d in [[0, 1, 0], [-1, 0, 1], [0, -1, 2], [1, 0, 3]]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N and board[ny][nx] == 0:
                if d == drc and cost + 100 <= costmap[ny][nx]:
                    q.append((nx, ny, cost + 100, d))
                    costmap[ny][nx] = cost + 100

                elif cost + 600 <= costmap[ny][nx] + 200:
                    q.append((nx, ny, cost + 600, d))
                    costmap[ny][nx] = cost + 600

    return costmap[N - 1][N - 1]


solution(
    [
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0],
    ]
)


# 각 지점에서 방향별로 큐에 넣는다.
# 내가 진행하려는 좌표에서의 값을 계산해봤을 때 지금 값보다 작으면 업데이트 시키고, 해당 좌표는 큐에 넣는다 (진행 가능)
# 골인지점에 도착했을 때 최솟값 출력
