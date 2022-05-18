# WIL : Week 8
8주차에 대한 WIL

# kakao_60057 : 문자열 압축
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/60057#

## 🥺 Unsolved Code

### 💻 Code

```python
def solution(s):
    answer = len(s)
    for l in range(1,int(len(s)/2)+1):
        idx = 0
        splited_s = []
        while idx < len(s):
            splited_s.append(s[idx:idx+l])
            idx += l
        length = 0
        curr = splited_s[0]
        count = 0
        for sub_s in splited_s:
            if curr == sub_s:
                count += 1
            elif count == 1:
                count = 1
                length += len(curr)
                curr = sub_s
            else:
                length += len(sub_s) + len(str(count))
                count = 1
                curr = sub_s
        length += len(sub_s)
        if count > 1:
            length += len(str(count))
        answer = min(answer, length)
    return answer
```

### ❗️ 결과

테스트 일부 실패

### 💡 접근

- 스트링을 1,2,3,...len(s)/2 로 쪼개는 순회를 진행한다
- 쪼갠 스트링 조각들은 리스트에 담는다
- 쪼갠 스트링 조각들을 순회하며 몇개의 패턴이 매칭되는지 counting 한다
- 패턴이 달라졌고, count == 1이면 `length += len(패턴)` 하고 패턴을 갱신한다
- 패턴이 달라졌고, count > 1 이면 `legnth += len(str(count)) + len(패턴)` 한다. (숫자와 문자 길이)(ex. aaa = 3a)
- 마지막에 남은 문자열 처리를 해주고, min함수로 최솟값을 갱신한다

### 🧐 접근에 대한 회고

분명 테스트 케이스는 다 맞는데 제출하면 틀린다. 아마 마지막 서브스트링 처리에서 문제가 생기는거 같은데 잘 못찾겠어서 좌절했다.

아마 내가 압축한 문자열을 실제로 구하지 않고 길이만 계산하는 구현을 해서 실제로 어떻게 작동하는지 제대로 파악이 안돼서 그랬던 것 같다.

그래서 홧김에 초기화 하고 처음부터 다시 짰다;;

## 😎 Solved Code

### 💻 Code

```python
def solution(s):
    answer = len(s)
    for l in range(1,int(len(s)/2)+1):
        encoded = ''
        idx = 0
        matched = s[:l]
        count = 0
        while idx < len(s):
            if matched == s[idx:idx+l]:
                count += 1
            else:
                if count > 1:
                    encoded += str(count) + matched
                else:
                    encoded += matched
                count = 1
                matched = s[idx:idx+l]
            idx += l
        if count > 1:
            encoded += str(count) + matched
        else:
            encoded += matched
        answer = min(answer, len(encoded))
    return answer
```

### ❗️ 결과

성공

### 💡 접근

동일하게 1~len(s)/2 까지 토막내는 순회로 인코딩을 진행한다. 대신 실제로 압축작업을 진행한 후, 그 문자열의 길이를 answer에 담았다.

문자열을 길이 l로 토막내서 미리 리스트에 저장하지 않고, idx라는 포인터와 idx+l 을 적절히 사용하여 순회로 구현했다.

- idx = 0, matched = s[:l]로 초기화한다
- 기본적으로 while문 안에서 `s[idx:idx+l]` 로 값을 확인하고,  `idx+=l` 연산을 하며 순회를 하는 로직을 짰다
- 순회하며 패턴(matched)와 일치하는 경우 count += 1 을 한다.
- 패턴과 달라지는 경우 `count > 1` 인경우와 `그렇지 않은 경우` 로 나누었다.
- 전자의 경우는 encoded += 3 + abc 와 같은 작업을, 후자는 encoded += abc 와 같은 작업을 한다.
- while문을 빠져나와 마지막에 처리하지 못 한 문자열을 처리해준다

## 🥳 문제 회고

정말 쉬울거라 생각하고 덤볐는데 생각보다 너무 오래걸렸다. 피지컬이 너무 약하다는걸 체감했다... 이런 구현 문제 실수없이 꼼꼼하게 빠르게 풀 수 있도록 많은 연습이 필요해보인다.

특히 포인터(인덱스)를 사용하는 구현은 실수할 여지가 많아서, 펜으로 꼼꼼하게 메모하면서 구현하자.

# kakao_64065 : 튜플
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/64065

## 😎 Solved Code

### 💻 Code

```python
def solution(s):
    answer = []
    s = s[2:-2].split("},{")
    ls = sorted([list(map(int, e.split(","))) for e in s], key=lambda x : len(x))
    answer.append(ls[0][0])
    prev_set = set(ls[0])
    for elem in ls[1:]:
        curr_set = set(elem)
        answer.append(list(curr_set - prev_set)[0])
        prev_set = curr_set
    return answer
```

### ❗️ 결과

성공

### 💡 접근

- s를 파싱해서 주어진 집합을 순서대로 2차원 리스트에 저장한 후, sorted로 길이순으로 오름차순 정렬한다
    - ex. [[2], [2, 1], [1, 2, 3], [1, 2, 4, 3]]
- 0번째 값을 answer에 넣고 1 ~ N까지 순회하며 `i+1번째 집합` - `i번째 집합` 원소를 append 한다

## 🥳 문제 회고

set의 차집합 연산을 이용해서 간단하게 중복 원소들을 제거할 수 있었다.

# kakao_67259 : 경주로 건설
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/67259

## 🥺 Unsolved Code

### 💻 Code

```python
def calc_cost(path):
    diff = []
    cost = 0
    for i in range(1,len(path)):
        diff.append((path[i][0] - path[i-1][0], path[i][1] - path[i-1][1]))
    curr = diff[0]
    for d in diff:
        if curr != d:
            cost += 500
        curr = d
    return cost + len(diff)*100

def solution(board):
    def dfs(y,x,path):
        global answer
        if y == N - 1 and x == N - 1:
            answer = min(answer, calc_cost(path))
            return
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<N and board[ny][nx] == 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                dfs(ny,nx,path+[(ny,nx)])
                visited[ny][nx] = False
        return
    global answer
    answer = int(1e10)
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    N = len(board)
    visited = [[False]*N for _ in range(N)]
    path = [(0,0)]
    visited[0][0] = True
    dfs(0,0,path)
    return answer
```

### ❗️ 결과

테스트 케이스부터 시간초과로 실패

### 💡 접근

단순 dfs로 완전탐색을 진행했다.

방문경로들을 path에 담아 (y,x)가 (N-1,N-1)에 도달하면 path를 가지고 cost를 계산한다.

글로벌 변수 answer에 가장 작은 cost를 업데이트한다.

### 🧐 접근에 대한 회고

dfs에 백트래킹을 넣어주면 해결할 수 있을 것 같다. 

하지만 이 쯤 됐을 때 백트래킹을 발생시킬 요인이 cost값이라는 걸 알게됐다. 이 코드는 마지막에 cost를 계산하는 로직이므로 노드를 계속 방문하며 cost를 계산하도록 수정이 필요했다.

몇가지 테스트 케이스를 생각하던 중 같은 노드에 대해 서로 다른 방향으로 접근한 cost가 같을 때, 그 이후의 움직임은 방향에 따라 달라진다는 것을 알게됐다.

결국 일반적인 dfs/bfs 문제처럼 y,x 좌표만 고려할 것이 아닌, **방향**이라는 변수도 고려해야 한다는 것이다.

이후에 dfs보다 bfs가 백트래킹에 더 구현이 쉬울 것 같아서 bfs로 갈아탔다.

처음에는 방향을 세로 == 1, 가로 == 0 로 갖는 2차원 리스트를 만들었는데... 테스트 25가 계속 실패가 떴다;;

왜인지는 이해할 수 없었다..ㅠ 조금 구글링 해본 결과 접근은 동일하나 구현이 다른 풀이를 발견했다. 기존 (y,x)를 담은 배열에 한 차원을 얹어 방향 정보까지 추가해 3차원 리스트로 풀었다.

아이디어를 빌려 3차원 리스트를 이용하는 bfs로 구현해봤다.

## 😎 Solved Code

### 💻 Code

```python
from collections import deque
INF = int(1e10)
def bfs(board,cost,N):
    global answer
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    cost[0][0][0] = cost[1][0][0] = 0
    q = deque([(0,0,0)])
    q = deque([(0,0,1)])
    while q:
        y, x, d = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            nd = i
            if 0<=ny<N and 0<=nx<N and board[ny][nx] == 0:
                c = cost[d][y][x] + 100
                if (x,y) != (0,0) and nd != d:
                    c += 500
                if c < cost[nd][ny][nx]:
                    cost[nd][ny][nx] = c
                    if ny == N-1 and nx == N-1:
                        answer = min(answer, c)
                    else:
                        q.append((ny,nx,nd))

def solution(board):
    global answer
    answer = INF
    N = len(board)
    cost = [[[INF]*N for _ in range(N)] for _ in range(4)]
    bfs(board,cost,N)
    return answer
```

### ❗️ 결과

성공

### 💡 접근

dy,dx 순서에 따라 0 : 우 / 1 : 하 / 2 : 좌 / 3 : 상 의 방향 정보를 갖는다.

3차원 리스트 cost의 1번째 인덱스는 위의 4방향 정보, 2,3번째는 (y,x)를 나타낸다.

bfs시에 시작 지점에서 우(0) / 하(1) 방향 두 군데로 시작할 수 있다.

따라서 queue에 (0,0,0), (0,0,1)을 넣어 시작한다.(y,x,방향)

나머지는 비용을 계산하고 해당 방향과 좌표의 노드의 비용보다 적을 경우 queue에 push 한다.

나름 queue push, pop 연산을 줄이고자 (y,x)가 (N-1,N-1)에 도달했을 때는 강제로 append하지 않고 answer값을 갱신하기만 한다.

## 🥳 문제 회고

평소 풀던 bfs / dfs 문제보다 생각이 많아졌던 문제였다. 방향이라는 조건 하나만 추가됐는데 체감 난이도가 급상승한 것 같다. 어렵게 해결했지만 좋은 문제라고 생각한다.