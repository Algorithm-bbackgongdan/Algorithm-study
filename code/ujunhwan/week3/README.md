<!-- @format -->

시간을 너무 잘못알았네요 ㅠㅠ 죄송합니다.......

드릴말씀이 없습니다....

# 1번

제가 푼 방식..

5x5 보고 완전탐색인거같아서 처음에 막 짰습니다.

마지막에 딱 걸린 사람이 지는 아이디어로 풀었습니다..

A -> B -> A -> B ... 반복되기 때문에 단순 카운팅만 진행하여도 어떤 순서인지 알 수 있습니다.

이기는게 그 전 노드에서 뒤집힌다는걸 생각 못해서 시간을 많이 썼던거같아요..

A 입장에서 이길 수 있다면 실수 안하면 무조건 이기는거니까 이기는거에 포커싱했습니다.

```python
win, result = dfs([ny, nx], bPos, count+1)
    board[ay][ax] = 1
    if win == 0:
        canWin = True
```

처음에 canWin = False로 초기화 해놓고.. 그 다음 노드 결과 중 지금 상태가 한번이라도 이기면 실수 안하면 이기는거니까 이렇게 다뤘습니다.

만약에 이길 수 있다면 항상 최소를 반환해야합니다.

코드 이쁘게 짜보겠다고 값을 나누지 않고 다뤘다가 큰 낭패를 보았읍니다..

그리고 이게 습관인지 모르겠는데

```
board[ny][nx] = 0
dfs()
board[ny][nx] = 1
```

이렇게 해놓고 발견 못해서 뻘짓도 했습니다.

## 2번

이건 그냥 시뮬레이션 문제같아서 돌려봤어요

이거 비슷한거 제가 sk ict 코테 1차에서 풀었던 문제보다 쉬운버전이라 금방 풀었던거같습니다..

회전할때는 반대방향으로 진행하며 다음값에 영향주지않게 땡겨주는게 이 문제 핵심인거같아요!

## 3번

재귀를 이용해서 문제에 나온대로의 논리를 전개해주는 문제인 것 같아요

딕테이션 같은 편리한 자료형 볼때마다 파이썬 사랑스럽습니다...

문제의 i번째 referral이 i번째 enroll의 부모 노드이므로, 이 부분을 처리해서 인접 노드에 넣어줬습니다.

데이터의 흐름 방향이 자식 -> 노드 이므로 adj[자식] = 부모 로 저장하였고,

자식 노드의 인덱스일 때 adj[index] 를 이용하여 나의 부모의 인덱스를 쉽게 알 수 있었습니다.

enroll이 인덱스 -> 사람이름 의 매핑이므로

{'사람이름' : index} 형식의 딕테이션을 새로 생성해서 이름과 인덱스를 매핑하였습니다.

```python
dic = {}
dic['-'] = -1
for i in range(size):
    dic[enroll[i]] = i
```

임의의 이름들도 등장하지만, - 도 부모가 없는 노드들을 나타내기 위해 등장하므로 -1로 예외처리 해주었스빈다.

마지막 12, 13번인가 시간초과 뜨길래 좀 고민하다가.. amount가 0일때 탐색할 필요없이 넘어갔스빈다.

그런데도 시간초과 뜨길래.. 왤까 왜지 0이어도 계속 부모노드로 가는구나 아 예외처리해야겠다 하고 풀었습니다..

카카오 풀다가 푸니까 좀 쉬운느낌의 문제였슴니다....
