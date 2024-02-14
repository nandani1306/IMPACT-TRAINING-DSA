# void cur(struct Node*node,int lvl){
#     if(root==NULL){
#         return;
#     }
#     if(lvl==1){
#         print(root->data)
#     }
#     else if(lvl>1){
#     }
# }

class Vertex:
    def __init__(self,data) -> None:
        self.left = None
        self.data = data
        self.right = None

def inorder(root):
    if root:    
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def preorder(root):
    if root:    
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:    
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

def insert(root,value):
    if root is None:
        return Vertex(value) 
    else:
        if value < root.data:
            root.left = insert(root.left, value) 
        elif value > root.data:
            root.right = insert(root.right, value) 
        return root 

def minElement(root):
    if root is None:
        return
    else:
        while root.left is not None:
            root = root.left
        print("Minimum lement is : ",root.data) 

def maxElement(root):
    if root is None:
        return
    else:
        while root.right is not None:
            root = root.right
        print("Maximum lement is : ",root.data) 

def search(root,target):
    if root is None or root.data == target:
        return root
    else:
        if root.data > target:
            return search(root.left,target)
        elif root.data < target:
            return search(root.right,target)
        
def inorderSucc(root):
    if root is not None and root.left is not None:
        root = root.left
    return root
        
def delete(root,targetDeletion):
    if root is None:
        return 
    if root.data == targetDeletion:
        # 0 child
        if root.left is None and root.right is None:
            root=None
            return 
        # 1 child
        elif root.left is None:
            temp = root.right
            root=None
            return temp
        
        elif root.right is None:
            temp = root.left
            root=None
            return temp
        
        else:
            temp = inorderSucc(root.right)
            root.data = temp.data
            root.right=delete(root.right,targetDeletion)
    elif root.data > targetDeletion:
        root.left = delete(root.left,targetDeletion)
    else:
        root.right = delete(root.right,targetDeletion)
    return root

root=Vertex(15)
insert(root,10)
insert(root,20)
insert(root,30)
minElement(root)
maxElement(root)
inorder(root)
# if(search(root,20) is None):
#     print("\nTarget is not found")
# else:
#     print("\nTarget is found")
inorder(root)
print("\n")
delete(root,20)
inorder(root)