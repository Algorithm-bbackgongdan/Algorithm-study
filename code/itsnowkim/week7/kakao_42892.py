import sys
sys.setrecursionlimit(10**6)
from functools import cmp_to_key

class Node:
    def __init__(self,item):
        self.item = item
        self.left = None
        self.right = None
    def add(self, node):
        if node.item[0] < self.item[0]:
            if self.left == None:
                self.left = node
            else:
                self.left.add(node)
        else:
            if self.right == None:
                self.right = node
            else:
                self.right.add(node)
                
class BinaryTree():
    def __init__(self): # 트리 생성
        self.root = None
    
    def preorder(self,n,lst):
        if n != None:
            # print(n.item,' ',end='')
            lst.append(n.item[2])
            if n.left:
                self.preorder(n.left,lst)
            if n.right:
                self.preorder(n.right,lst)
    
    def postorder(self,n,lst):
        if n != None:
            if n.left:
                self.postorder(n.left,lst)
            if n.right:
                self.postorder(n.right,lst)
            # print(n.item,' ',end='')
            lst.append(n.item[2])

def xy_compare(a,b):
    if a[1] < b[1]:
        return 1
    elif a[1] == b[1]:
        if a[0] > b[0]:
            return 1
        else:
            return -1
    else:
        return -1

def solution(nodeinfo):
    # input 정리
    for idx,tmp in enumerate(nodeinfo):
        tmp.append(idx+1)
    nodeinfo = sorted(nodeinfo, key=cmp_to_key(xy_compare))
    
    # init binary tree
    tree = BinaryTree()
    tree.root = Node(nodeinfo[0])
    # make tree
    for node in nodeinfo[1:]:
        tree.root.add(Node(node))
    
    pre=[]
    post=[]

    tree.preorder(tree.root,pre)
    tree.postorder(tree.root,post)
    
    return [pre,post]