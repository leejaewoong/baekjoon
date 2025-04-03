# 문제 링크: https://www.acmicpc.net/problem/1991

from collections import defaultdict
import sys
input = sys.stdin.readline

nodeN = int(input())
tree = defaultdict(list)
for i in range(nodeN):
    a, b, c = input().split()
    tree[a] = [b, c]


def preorder(tree, node):
    result = []
    result.append(node)

    left, right = tree[node]
    
    if left != '.':
        result += preorder(tree, left)

    if right != '.':
        result += preorder(tree, right)  

    return result


def inorder(tree, node):
    result = []    

    left, right = tree[node]
    
    if left != '.':
        result += inorder(tree, left)

    result.append(node)

    if right != '.':
        result += inorder(tree, right)  

    return result


def postorder(tree, node):
    result = []    

    left, right = tree[node]
    
    if left != '.':
        result += postorder(tree, left)    

    if right != '.':
        result += postorder(tree, right)  
    
    result.append(node)

    return result


print(''.join(preorder(tree, 'A')))
print(''.join(inorder(tree, 'A')))
print(''.join(postorder(tree, 'A')))




    

