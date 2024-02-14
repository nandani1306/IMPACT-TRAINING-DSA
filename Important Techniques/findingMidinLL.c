#include<stdio.h>
#include<stdlib.h>

struct Node
{
    int data;
    struct Node *link;  
};

typedef struct Node Node;
Node *head = NULL;

Node *newNode(int value){
    Node *temp = (Node*)malloc(sizeof(Node));
    if (temp == NULL){
        printf("No memory allocated\n");
    }
    temp->data = value;
    temp->link = NULL;
    return temp;
}

int insertAtBeginSingle(int value){
    if(head == NULL){
        head = newNode(value);
    }
    else{
        Node *temp = newNode(value);
        temp->link = head;
        head = temp;
    }
}

int findMid(){
    Node* slow = head;
    Node* fast = head;

    if(!head){
        return -1;
    }
    else if ((head->link == NULL) || (head->link->link == NULL)){
        return head->data;
    }
    else{
        while ((fast->link != NULL) && (fast->link->link != NULL))
        {
            slow = slow->link;
            fast = fast->link->link;
        }
        return slow->data;  
    }   
}

int main(){
    insertAtBeginSingle(12);
    insertAtBeginSingle(17);
    insertAtBeginSingle(15);
    insertAtBeginSingle(55);
    insertAtBeginSingle(35);
    insertAtBeginSingle(25);
    printf("%d",findMid());
}