class Node:
    def __init__(self,root,left,right):
        self.root = root
        self.left = left
        self.right = right

def inorder(node):
    print(node.root,end='')
    if node.left!='.':
        inorder(tree[node.left])
    if node.right!='.':
        inorder(tree[node.right])

def preorder(node):
    if node.left!='.':
        preorder(tree[node.left])
    print(node.root,end='')
    if node.right!='.':
        preorder(tree[node.right])

def postorder(node):
    if node.left!='.':
        postorder(tree[node.left])
    if node.right!='.':
        postorder(tree[node.right])
    print(node.root, end='')

n = int(input())
tree = {}
for i in range(n):
    root,left,right = input().split()
    tree[root]= Node(root,left,right)

inorder(tree['A'])
print()
preorder(tree['A'])
print()
postorder(tree['A'])