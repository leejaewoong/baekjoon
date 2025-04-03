from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

preorder = []

while True:
    try:
        preorder.append(int(input()))
    except:
        break

def getTree(preorder):
    tree = defaultdict(list)

    if len(preorder) > 1:
        for i in range(1, len(preorder)):
            if preorder[i] < preorder[i-1]:
                tree[preorder[i-1]].append(preorder[i])
            else:
                tree[preorder[i-1]].append('.')
                temp = []
                for j in preorder[:i]:
                    if j < preorder[i]:
                        temp.append(j)                 
                tree[max(temp)].append(preorder[i])                

        for node in preorder:
            if node not in tree:
                tree[node] = ['.', '.']
            elif len(tree[node]) == 1:
                tree[node].append('.')
            elif len(tree[node]) == 0:
                tree[node] = ['.', '.']

        return tree
        
    else:
        return preorder
    

result = getTree(preorder)


def postorder(preorder, root):    
    result = []        

    left, right = preorder[root]

    if left != '.':
        result += postorder(preorder, left)

    if right != '.':
        result += postorder(preorder, right)

    result.append(root)
    return result

ans = postorder(result, preorder[0])


for i in ans:
    print(i)


    



