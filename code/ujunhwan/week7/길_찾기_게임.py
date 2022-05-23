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
        
        number = -1
        idx = -1
        max_y = -1
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