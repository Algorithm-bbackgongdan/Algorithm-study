# 60057 - 문자열 압축
[문제출처](https://programmers.co.kr/learn/courses/30/lessons/60057)

## 풀이시간
1시간. 역시 문제 이해를 잘못했었음.
왜냐면 당연히 압축하면, 압축을 해제할 때 압축된 결과물을 보고 되돌릴 수 있어야 하는데,
이 경우에 그게 보장이 안된다. 그래서 문제 이해하는데 오래 걸렸다.

풀이는 사실 어떤 알고리즘으로 분류해야 할 지 모르겠는게, 그냥 하라는 대로 했다...

# 64065 - 튜플
[문제출처](https://programmers.co.kr/learn/courses/30/lessons/64065)

## 풀이시간
잘 기억 안나는데 금방 해결했다. `python`은 in, not in이 너무 사기적인것같다..

## 검색한거
- `lambda` 문법이 잘 기억이 안나서 검색했다.

# 67259 - 경주로 건설
[문제출처](https://programmers.co.kr/learn/courses/30/lessons/67259)

## 풀이시간
3일. 종이에 정말 많이 써가면서 고민 많이 했고, 실제 코드로 옮기는 것도 시행착오를 너무 많이 겪었다.

## 검색한거
- `bfs`, `dp in python`
처음에는 단순하게 '최단거리' 로만 생각하고 오른쪽, 아래쪽 방향 두 가지만 있으면 되겠네, 했다가 아님을 깨달았다.
벽이 있기 때문에 위로 갈 수도, 왼쪽으로 갈 수도 있기 때문이다.

그 다음으로 떠올린 것은 '그래프 문제' 로 생각하고 벽을 사이에 둔 지점 사이 거리를 INF로 생각하고
그래프를 이었을 때 최단 비용이 나오도록 설계하면 되지 않을까? -> 이 알고리즘의 이름이 정확히 기억나지 않는다..
했는데, 이 문제도 불가능한 점이 있었다. 이전 지점에서 다른 지점으로 이동할 때의 방향을 저장할 수가 없었다,,,

그렇다면 어떻게 해야 할까.

멍청하지만 확실한 방법으로 가보자.
어떻게 가지? `bfs`, `dfs` 로 탐색을 해볼까? 금방 `dfs` 는 불가능함을 알았다.
탈출조건에서 `dfs` 순회를 마치면, 다른 경우의 수를 살펴볼 수 없기 때문이다.

`bfs`는 가능한가? 가능하다!

다음은 내 알고리즘이다.

1. 출발지점에서 queue에 다음으로 이동할 가능성이 있는 지점을 넣는다.
2. 다음 지점에서 상하좌우를 살피고, 최단비용으로 올 수 있는 방향에서 왔다고 표시한다.
이 때, 하나 이상의 방향에서 왔다고 가정해도 같은 비용으로 판단된다면 두 가지 방향 모두 저장한다.
3. 1로 돌아가서 반복하되, 도착지점에 도달했을 경우 탈출한다.

아직 코드로의 구현은 하는 중이다...

```python
# 처음에는 오른쪽이나 아래 둘 중 하나로 무조건 이동함
    if board[0][1] != 1:
        visited[0][1] = 1
        direction[0][1] = 'r'
        queue.append((0,1))
    if board[1][0] != 1:
        visited[1][0] = 1
        direction[1][0] = 'd'
        queue.append((1,0))
```
처음 시도했을 때 다음과 같이 두 가지를 넣고 시작했는데, direction check를 할 때
direction배열에 저장해서 돌리면 하나의 방향만 저장하게 되는데, 따라서 경우의 수가 여러개일 경우
다른 경우의 수를 무시하게 된다.
그래서 direction 또한 여러 방향을 고려해야 했다.

놀라운 사실....
장장 4시간에 걸쳐 a4 4 장과 수많은 print로 디버깅을 하던 결과...
충격적인 코드를 발견했다.
```python
 # 오른쪽, 왼쪽, 아래, 위 순서로 테스트
        for move in movement:
            new_x = x + move[0]
            new_y = x + move[1]
            new_dir = move[2]
```
y값 업데이트를 x로 하고 있었네용?
ㅎㅎㅎㅎ깔깔...

거짓말처럼 y로 바꾸니까 테스트 성공....

괜찮다... 나는 시간낭비라고 생각하지 않는다...
정말 많이 읽어봤고, 정말 많이 생각했기 때문에
비슷한 문제를 앞으로 만난다면 그 때는 쉽게 풀지 않을까.

그러나 이렇게 제출하면 5개 케이스에서 틀린다. 이유가 뭘까..

