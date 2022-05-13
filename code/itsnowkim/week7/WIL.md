# 1번
[문제출처](https://programmers.co.kr/learn/courses/30/lessons/42888)
## 풀이시간

정확히 재지는 않았는데 15~20분 정도 걸린 듯.
문제 보고 이해하고 설계하는 시간 5분, 구현 나머지인듯.

`python` 으로 코테 준비 시작한지 얼마 안되어서 
어떻게 해야 할지 알긴 아는데 문법이 익숙하지 않아서 오래 걸린 듯.

## 검색한거

- 문자열 `split` 하는 함수.
많이 쓰여서 존재를 알고 있었는데 문법이 확실하지 않아서 검색함.

- `hash` -> `python` 에서는 `dictionary` 를 사용한다.
이것도 존재는 알고 있었는데 문법이 확실하지 않아서 검색했다.
`dictionary` 에 값을 추가하고 가져오기를 검색함.

- `replace` 함수
원래는 `history` 에 배열 형태로 id, 행동 이렇게 저장 안하고
id+행동 string으로 저장했는데, 이러면 마지막에 id를 replace하는 부분이 어려울 것 같아서
바로 배열로 바꿔서 저장했다.

## 추가로 알게된거
`dictionary` 에 접근하고자 하는 `key` 값이 없으면
keyError가 나오니까 try except로 하던지,
dictionary.get() 내장함수로 값을 가져오자.

# 2번
[문제출처](https://programmers.co.kr/learn/courses/30/lessons/42892)

## 풀이시간
30분 정도?
어떻게 풀어야겠다 떠올린건 5분 남짓, 구현이 오래 걸림

## 검색한거

- 특정 조건에 따라 정렬하는 방법
`cmp_to_key` 써서 정렬했다.
사실 단순 sort()만 썼다가 최근에 `lambda`를 알게 되어서 이걸 쓰려고 했는데 조건이 두개라서
"파이썬 여러 조건으로 정렬하기" 했더니 나오더라.
역시 파이썬은 최고야
[cmp_to_key](https://pearlluck.tistory.com/599) 여기 참고함

- 이진트리 구현하기
파이썬에서 만들어 본 적이 없어서 검색했다.
[이진트리만들기](https://it-garden.tistory.com/406) 여기 참고해서 살짝 바꿔서 구현했다. 왼쪽, 오른쪽에 바로 추가하면 될 줄 알았는데, depth가 깊어지는 경우가 있더라. 그래서 그 부분을 재귀로 구현해서 추가해줬다.

## 추가로 알게된거
다 잘 되는데 testcase 6, 7번이 안되더라. 보니까
```python
import sys
sys.setrecursionlimit(10**6)
```
이거 해주면 된다고 해서 했더니 됐다.

# 3번
[문제출처](https://programmers.co.kr/learn/courses/30/lessons/42890)

## 풀이시간

겁나어려움. 읽었을 때는 쉬웠는데 하루 넘게 고민한듯.

```python
from itertools import combinations
def solution(relation):
    answer = 0
    
    # column의 개수가 key의 원소의 개수가 될 수 있다.
    N = len(relation[0])
    
    # checklist - 이미 key가 되어버린 것은 다른 곳에 참여 불가능
    checklist = [0 for i in range(N)]
    
    # 원소의 개수가 1, 2, 3 순으로 증가시키면서 key가 될 수 있는 값들 확인
    for elementNum in range(1,N+1):
        hash_table = {}
        # print(hash_table)
        for rel in relation:
            c = list(combinations(rel, elementNum))        
            for group in c:
                key = ''.join(group)
                try:
                    if hash_table[key]:
                        hash_table[key].append(key)
                except KeyError:
                    hash_table[key] = [key]
        
    return answer
```
처음에는 이렇게 시도했는데, key값에 해당하는 value가 2개 이상이면 중복이기 때문에 제외시키면 되겠구나 생각했다.
그러나 hash_table에 생기는 key 값이 몇 번째 index인지도 알아야 판정이 가능한데, 그걸 어떻게 엮을지 몰라서 시간을 많이 썼다.

```python
from itertools import combinations

def solution(relation):
    answer = 0
    
    # column의 개수가 key의 원소의 개수가 될 수 있다.
    N = len(relation[0])
    M = len(relation)
    
    # checklist - 이미 key가 되어버린 것은 다른 곳에 참여 불가능
    checklist = [0 for i in range(N)]
    
    # 원소의 개수가 1, 2, 3 순으로 증가시키면서 key가 될 수 있는 값들 확인
    for elementNum in range(1,N+1):
        hash_table = {}
        key_list = []
        # print(hash_table)
        for rel in relation:
            c = list(combinations(rel, elementNum))
            index_num = list(combinations(range(N), elementNum))
            for idx, group in enumerate(c):
                value = ''.join(group)
                key = ''.join(''.join(map(str, index_num[idx])))
                if key not in key_list:
                    key_list.append(key)
                
                # hash_table 만들기
                try:
                    if hash_table[key]:
                        if value not in hash_table[key]:
                            hash_table[key].append(value)
                except KeyError:
                    hash_table[key] = [value]
                    
        # hash_table에서 key해 해당하는 배열 길이가 relation개수이면 걔는 key.
        for key in key_list:
            if len(hash_table[key]) == M:
                templist = list(key)
                count = 0
                for t in templist:
                    if checklist[int(t)] == 1:
                        break
                    else:
                        count+=1
                if count == len(templist):
                    answer += 1
                
                for t in templist:
                    if count == len(templist):
                        checklist[int(t)] = 1
                    
        # print(answer)
        # print(key_list)
        # print(hash_table)
        # print(checklist)
    return answer
```
눈물겨운 도전기...
애매하게 아예 틀리면 모르겠는데, 46.4점이 나온다.
도대체 어디가 틀린걸까... 계속 고민해봐야겠다.

## 검색한거

- `combination(list,N)` 
리스트 내에서 가능한 조합을 리턴해준다. 보통 list()로 감싸서 쓴다.

- `int` 형 리스트 `join`하기
무지성 join하면 에러뜬다. str내놔! 이러면서...

```python
num_list = [-1, 0, 1, 3, 4, 5, 9]

print(num_list)
# [-1, 0, 1, 3, 4, 5, 9]
print(" ".join(map(str, num_list)))
# -1 0 1 3 4 5 9

# print(" ".join(num_list))
# TypeError: sequence item 0: expected str instance, int found
```


## 추가로 알게된거
`dictionary` 에 접근하고자 하는 `key` 값이 없으면
keyError가 나오니까 try except로 하던지,
dictionary.get() 내장함수로 값을 가져오자.

