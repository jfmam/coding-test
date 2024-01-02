import sys
input = sys.stdin.readline

n = int(input())
a = {} # 결국 객체에 current, left child, right child를 저장

for _ in range(n):
    item,left,right = input().split()
    a[item] = [item,left,right]

def preorder(current):
    print(a[current][0],end='')
    if a[current][1] != '.':
        preorder(a[current][1])
    if a[current][2] != '.':
        preorder(a[current][2])
def inorder(current):
    if a[current][1] != '.':
        inorder(a[current][1])
    print(a[current][0],end='')
    if a[current][2] != '.':
        inorder(a[current][2])
def postorder(current):
    if a[current][1] != '.':
        postorder(a[current][1])
    if a[current][2] != '.':
        postorder(a[current][2])
    print(a[current][0],end='')
preorder('A')
print()
inorder('A')
print()
postorder('A')