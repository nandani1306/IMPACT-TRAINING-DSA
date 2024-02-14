#include<stdio.h>
#include<stdlib.h>

typedef struct Vertex
{
    int data;
    struct Vertex *lchild;  
    struct Vertex *rchild;  
} Vertex;

Vertex *newVertex(int value){
    Vertex *temp = (Vertex*)malloc(sizeof(Vertex));
    if (temp==NULL){
        printf("No memory allocated\n");
    }
    temp->lchild = NULL;
    temp->data = value;
    temp->rchild = NULL;
    return temp;
}

Vertex* root = NULL;

void inorder(Vertex* root){
    if(root==NULL)
        return;
    inorder(root->lchild);
    printf("%d ",root->data);
    inorder(root->rchild);
}

int minElement(Vertex* root){
    if(root==NULL){
        return 0;
    }
    else{
        while(root->lchild!=NULL){
            root=root->lchild;
        }
        return root->data;
    }
}

int maxElement(Vertex* root){
    if(root==NULL){
        return 0;
    }
    else{
        while(root->rchild!=NULL){
            root=root->rchild;
        }
        return root->data;
    }
}
Vertex* inorderSuccessor(Vertex* root){
    if(root!=NULL && root->lchild!=NULL){
        root=root->lchild;
    }
    return root;
}

Vertex* deleteElement(Vertex* root, int target){
        Vertex* temp;
        if(root == NULL){
            return 0;
        }
        if(root->data == target){
            //0 child
            if(root->lchild==NULL && root->rchild==NULL){
                free(root);
                return NULL;
            }

            //1 child
            else if (root->lchild==NULL)
            {
                temp=root->rchild;
                free(root);
                return temp;
            }
            else if(root->rchild==NULL){
                temp=root->lchild;
                free(root);
                return temp;
            }
            else{
                temp = inorderSuccessor(root->rchild);
                root->data = temp->data;
                root->rchild=deleteElement(root->rchild,target);
            }
        }
        //2 child
        else if(root->data > target){
            //left side data
            root->lchild = deleteElement(root->lchild,target);
        }
        else{
            //right side data
            root->rchild = deleteElement(root->rchild,target);
        }
    return root;
}

int height(Vertex* root){
    if (root == NULL){
        return 0;
    }
    else{
        int lheight = height(root->lchild);
        int rheight = height(root->rchild);

        if(lheight > rheight){
            return lheight+1;
        }
        else{
            return rheight+1;
        }
    }
}

Vertex* insert(Vertex* vertex, int value){
    if (vertex == NULL){
        return newVertex(value);
    }
    else{
        if(value < vertex->data){
            vertex->lchild = insert(vertex->lchild,value);
        }
        else if (value > vertex->data){
            vertex->rchild = insert(vertex->rchild,value);
        }
    }
}

Vertex* search(Vertex* vertex, int target){
    if(vertex == NULL || vertex->data == target){
        return vertex;
    }
    if (target < vertex->data)
    {
        return search(vertex->lchild, target);
    }    
    else if(target > vertex->data){
        return search(vertex->rchild, target);
    }
    else{
        return NULL;
    }
}

int main(){
    root = newVertex(10);
    
    int ch,target,val;
    while(ch!=8){
        printf("1]Insert 2]Search 3]Print 4]Min 5]Max 6]Height 7]Delete 8]Exit\n");
        printf("Enter choice: \n");
        scanf("%d",&ch);
        switch(ch){
            case 1:
                printf("Enter Node data:");
                scanf("%d",&val);
                insert(root,val);
                break;

            case 2:
                printf("Enter searching element:");
                scanf("%d",&target);
                // search(root,target);
                if (search(root, target) == NULL){
                    printf("%d not found\n", target);
                }
                else{
                    printf("%d found\n", target);
                }
                break;

            case 3:
                inorder(root);
                printf("\n");
                break;
            case 4:
                printf("Min element is : %d\n",minElement(root));
                break;
            case 5:
                printf("Max element is : %d\n",maxElement(root));
                break;
            case 6:
                printf("Height of tree is : %d\n",height(root));
                break;
            case 7:
                inorder(root);
                printf("\n");
                int tar;
                printf("Enter element to delete:\n");
                scanf("%d",&tar);
                deleteElement(root,tar);
                inorder(root);
                printf("\n");
                break;
            }
        }
    return 0;
}