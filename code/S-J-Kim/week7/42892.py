import sys

sys.setrecursionlimit(10 ** 6)


def post(vertices, answer):
    root = vertices[0]
    lst, rst = [], []

    for vertex in vertices[1:]:
        if root[0] > vertex[0]:
            lst.append(vertex)
        else:
            rst.append(vertex)

    if len(lst):
        post(lst, answer)
    if len(rst):
        post(rst, answer)

    answer.append(root[2])


def pre(vertices, answer):
    root = vertices[0]
    lst, rst = [], []

    for vertex in vertices[1:]:
        if root[0] > vertex[0]:
            lst.append(vertex)
        else:
            rst.append(vertex)

    answer.append(root[2])

    if len(lst):
        pre(lst, answer)
    if len(rst):
        pre(rst, answer)


def solution(nodeinfo):

    postans, preans = [], []
    nodeinfo = [[x, y, i + 1] for i, [x, y] in enumerate(nodeinfo)]
    nodeinfo.sort(key=lambda x: (-x[1], x[0]))

    post(nodeinfo, postans)
    pre(nodeinfo, preans)

    return [pre, post]


solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]])


# 좌표를, y, x 순으로 정렬한다
# y가 같은 애들끼리 정렬을 한다
# 나보다 한단계 낮은 애들 중에 나의 x값보다 작으면 left, 크면 right -> visited에 넣어서 중복 선택 방지

# 그런 다음에 후위, 전위 순회
