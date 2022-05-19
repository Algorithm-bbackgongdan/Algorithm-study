# WIL : Week 7
7주차에 대한 WIL

## 재귀 함수 depth 늘려주기
```python
import sys
sys.setrecursionlimit(10**6)
```
호출 가능한 재귀 함수 수 초과시, 제출시에 런타임 에러라 찍힌다.
어떤 에러인지 모르면 삽질 할 수 있으니 재귀 함수를 쓸 상황이면 미리 limit을 풀어주자.

# kakao_42888 : 오픈채팅방
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42888

## 😎 Solved Code

### 💻 Code

```python
def solution(record):
    answer = []
    nickname = {}
    for r in record:
        data = r.split(" ")
        if data[0] == "Leave":
            continue
        nickname[data[1]] = data[2]
    
    for r in record:
        data = r.split(" ")
        if data[0] == "Leave":
            msg = f"{nickname[data[1]]}님이 나갔습니다."
        elif data[0] == "Enter":
            msg = f"{nickname[data[1]]}님이 들어왔습니다."
        else:
            continue
        answer.append(msg)
    return answer
```

### ❗️ 결과

성공

### 💡 접근

- record 순회로 최종적으로 변경된 닉네임 정보를 저장한다
- record를 순회하며 메세지를 출력한다

## 🥳 문제 회고

단순한 구현 문제였다

# kakao_92890 : 후보키
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/92890

## 😎 Solved Code

### 💻 Code

```python
from itertools import combinations

def is_unique(atts, relation):
    tmp = []
    for r in relation:
        row = tuple(r[i] for i in atts)
        tmp.append(row)
    
    return len(set(tmp)) == len(tmp)

def solution(relation):
    atts_num = len(relation[0])
    unique_atts = []
    
    for i in range(1,atts_num+1):
        for atts in combinations(range(atts_num), i):
            # 유일성 검사
            if not is_unique(atts, relation):
                continue
            # 최소성 검사
            for uni in unique_atts:
                if len(uni - set(atts)) == 0:
                    break
            else:
                unique_atts.append(set(atts))
                
    return len(unique_atts)
```

### ❗️ 결과

성공

### 💡 접근

- 1 ~ N 개의 속성들을 선택한다 (combinations 이용)
- 유일성 검사 진행 → 통과시 최소성 검사로 넘어간다
    - 유일성 검사는 `is_unique` 메소드에서 진행한다
    - 선택한 속성들의 row들을 tmp에 저장한 뒤, set(tmp) 와 len(tmp)를 비교한다
    - 집합은 고유한 원소를 저장하므로 값이 다르면 False를 리턴한다
- 최소성 검사 통과시 unique_atts.append(set(atts))로 attribute 튜플을 set 형태로 저장 (for-else 구문)
    - 최소성 검사는 unique_atts를 순회하며 진행한다
    - unique_atts의 원소 uni는 속성들의 집합(set)이다
    - uni - set(atts) 시에 공집합이라면 최소성 검사에 실패하므로 break 후 다음 iteration으로 넘어간다

## 🥳 문제 회고

set 자료구조를 이용하여 쉽게 중복값 체크를 할 수 있었다.

# kakao_42892 : 길 찾기 게임
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42892

## 😎 Solved Code

### 💻 Code

```python
import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, x,y,n):
        self.num = n
        self.x = x
        self.y = y
        self.left = None
        self.right = None
        
    def push(self, node):
        if node.x < self.x:
            if self.left == None:
                self.left = node
            else:
                self.left.push(node)
        else:
            if self.right == None:
                self.right = node
            else:
                self.right.push(node)
    
    def pre_traversal(self):
        global pre
        pre.append(self.num)
        if self.left:
            self.left.pre_traversal()
        if self.right:
            self.right.pre_traversal()
    
    def post_traversal(self):
        global post
        if self.left:
            self.left.post_traversal()
        if self.right:
            self.right.post_traversal()
        post.append(self.num)

def solution(nodeinfo):
    global pre, post
    pre = []
    post = []
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1) # node number
    n = sorted(nodeinfo, key=lambda x : (-x[1], x[0]))
    root = Node(n[0][0], n[0][1], n[0][2])
    
    for x, y, num in n[1:]:
        newNode = Node(x,y,num)
        root.push(newNode)
    
    root.pre_traversal()
    root.post_traversal()
    
    return [pre,post]
```

### ❗️ 결과

성공

### 💡 접근

- nodeinfo의 원소마다 노드 번호를 추가한다
- sorted(nodeinfo, key=lambda x : (-x[1], x[0])) 로 정렬한다
    - y (x[1])에 대해 내림차순 정렬 & x (x[0])에 대해 오름차순 정렬
- root 노드를 첫번째 원소로 만든다
- n[1:] 을 순회하며 남은 노드들을 push 하며 tree를 만든다
- 재귀함수로 구현한 pre_traversal, post_traversal 메소드로 전위, 후위 순회를 한다

## 🥳 문제 회고

자료구조 수업때 배우고 c로 구현해봤을 트리다. c언어로 트리 구현은 해봤어도 파이썬은 처음인데 c랑 다르게 포인터를 잘 사용하지 않다보니 모든 로직을 재귀로 처리해야했다.

재귀로 구현하다가 계속 제출시 몇 개 에러가 떴는데, 재귀 호출 depth를

```python
import sys
sys.setrecursionlimit(10**6)
```

요렇게 풀어주면 해결 가능하다.

오랜만에 트리 구현할 수 있니? 라고 물어보는 것 같았던 문제.