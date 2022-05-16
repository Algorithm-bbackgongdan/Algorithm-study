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