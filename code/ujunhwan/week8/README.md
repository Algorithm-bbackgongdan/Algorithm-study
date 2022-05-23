<!-- @format -->

# 경주로\_건설.py

한 위치에서 자동차의 방향이 어떤가에 따라서 코스트가 달라지는 것을 알 수 있습니다.
격자가 아니고, cost가 존재하므로 다익스트라를 사용하여 최단거리를 구했는데, 방향 정보까지 기록하는 2차원 배열을 사용하여 문제를 풀었습니다.

```python
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
```

# 문자열\_압축.py

이건 그냥 후루룩

```python
def solution(string):
    answer = len(string)
    length = len(string)
    for num in range(1, length+1):
        cnt = 0
        cand = 0
        prev = string[0:num]
        last_idx = 0
        for i in range(0, length, num):
            last_idx = i
            if prev == string[i:i+num]:
                cnt += 1
            elif cnt >= 2:
                if cnt < 10:
                    cand += (1+num)
                elif cnt < 100:
                    cand += (2+num)
                elif cnt < 1000:
                    cand += (3+num)
                else:
                    cand += (4+num)
                prev = string[i:i+num]
                cnt = 1
            else:
                prev = string[i:i+num]
                cand += num
                cnt = 1

        if cnt >= 2:
            if cnt < 10:
                cand += (1+num)
            elif cnt < 100:
                cand += (2+num)
            elif cnt < 1000:
                cand += (3+num)
            else:
                cand += (4+num)
        else:
            cand += (length - last_idx)

        if answer > cand:
            answer = cand

    return answer
```

# 튜플.py

길이를 기준으로 오름차순 정렬을 한다.  
하나의 튜플을 샐 때, 이번 튜플에서 생긴 값들을 저장하는 카운트와 지금까지 나온 값들을 저장하는 딕셔너리 를 서로 비교를 해준다.

만약 카운트 값이 더 크다면, 이전에 나오지 않은 값이므로 저장해주는 방식으로 풀었다.

```python
def solution(s):
    s = s.split('},')
    for i, p in enumerate(s):
        s[i] = p.split(',')
    for i, p in enumerate(s):
        for ii, f in enumerate(p):
            p[ii] = f.replace('{', '').replace('}', '')

    answer = []

    s.sort(key=lambda x:len(x))
    dic = dict()

    for p in s:
        for f in p:
            cnt = dict()
            if f not in dic:
                dic[f] = 0
            if f not in cnt:
                cnt[f] = 0
            cnt[f] += 1
            if cnt[f] > dic[f]:
                dic[f] += 1
                answer.append(int(f))

    print(dic)
    return answer
```
