<!-- @format -->

# 길\_찾기.py

처음에 좀 헤맸어요.

트리를 만드는게 관건인 문제인 것 같아 어떻게 만들지 막 해봄..

우선순위큐에 넣어서 y순서대로 정렬하고

쭉 내려서 뭔가를 해보려고 했는데, y값이 비어있는 곳도 있고..

아 x값으로 해야되나? 하고 정렬한 다음에 문제 뚫어져라 쳐다보다가

현재 노드의 왼쪽 중 가장 y가 큰 노드가 왼쪽 자식노드

현재 노드의 오른쪽 중 가장 y가 큰 노드가 오른쪽 자식노드

이 두가지를 이용해서 풀었어요.

인덱스 구간 설정을 하는데 닫힌구간할지 열린구간할지 하다가 열린걸로 하고 예외처리 넣어줬습니다.

```python
import bisect as bs
import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    N = len(nodeinfo)

    for i, info in enumerate(nodeinfo):
        x, y = info
        nodeinfo[i] = [x, y, i+1]

    nodeinfo.sort()
    #print(nodeinfo)

    '''
    왼쪽 중 가장 y가 큰 것 -> 왼쪽 자식
    오른쪽 중 y가 가장 큰 것 -> 오른쪽 자식
    lo ~ hi 까지 검색 lo hi 유효값
    '''

    node = [[-1, -1] for _ in range(N+1)]

    def make_tree(lo, hi):
        if lo > hi or lo < 0 or lo > N or hi < 0 or hi > N:
            return -1

        number = -1 # root number
        idx = -1 # root index
        max_y = -1 # root y
        for i in range(lo, hi+1):
            x, y, n = nodeinfo[i]
            if max_y < y:
                max_y = y
                number = n
                idx = i

       	left_child = make_tree(lo, idx-1)
        right_child = make_tree(idx+1, hi)
        node[number] = [left_child, right_child]
        return number

    pre = []
    def preorder(num):
        left, right = node[num]
        pre.append(num)
        if left != -1:
            preorder(left)
        if right != -1:
            preorder(right)

    post = []
    def postorder(num):
        left, right = node[num]
        if left != -1:
            postorder(left)
        if right != -1:
            postorder(right)

        post.append(num)

    root = make_tree(0, N-1)
    preorder(root)
    postorder(root)
    answer = [pre, post]
    return answer
```

# 오픈\_채팅방.py

이건 그냥 풀었음

# 후보키.py

이거 처음 접근을 1개부터 선택한 뒤 visited를 이용해서 후보키를 이루는 컬럼들이

하나라도 선택된적이 있으면 (이미 조합이 된 경우라면) 스킵하게 만들었었는데

절반만 맞더라고요.. 제가 문제를 잘못 본듯;;; uniqueness를 만족하는 부분은 잘 처리 했는데

최소성에 대한 부분이 잘못 되었었습니다.

[0] 이 후보키가 되지 않았을 때, [0, 1], [0, 2] 도 될 수 있는건데

제가 짠 코드에선 [0, 1]이 되면 [0, 2]는 선택되지 않는다는 오류를 발견했습니다.

그래서 모든 부분 집합을 전부 검사하도록 했습니다..

```python

from itertools import combinations

def solution(relation):
    C = len(relation[0])
    R = len(relation)

    def check(comb):
        dic = dict()
        for i in range(R):
            s = ""
            for j in comb:
                s += (relation[i][j] + "//")
            if s not in dic:
                dic[s] = 0
            dic[s] += 1
        return max(dic.values()) == 1

    # uniqueness
    uniq = []
    for level in range(1, C+1):
        comb = list(combinations(range(C), level))
        for c in comb:
            #print(list(c))
            if check(c):
                uniq.append(list(c))

    # print(uniq)

    # minimality
    answer = []

    def exam(lst):
        for i in range(len(lst)):
            for c in combinations(lst, i):
                # c 가 모든 부분집합
                if list(c) in answer:
                    return False
        return True

    for comb in uniq:
        if exam(comb):
            # 모든 부분집합을 검사 ?
            answer.append(comb)

    #print(answer)
    return len(answer)

```

개인적으로 이 문제가 제일 어려웠습니다.. ㅠㅠ
