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
        Node *temp = newNode(20);
        temp->link = head;
        head = temp;
    }
}

void insertAtBeginCirc(int value){
    Node* temp1 = newNode(value);
    if(head == NULL){
        head = temp1;
        head->link = head;
    }
    else{
        Node* temp = head;
        while(temp->link != head)
        {   
            temp = temp->link;
        }
        temp->link = temp1;
        temp1->link = head;
        head = temp1;
    }
}

int detectCycle(){
    Node* slow = head;
    Node* fast = head;

    while(slow != NULL && fast != NULL && fast->link != NULL) {
        slow = slow->link;
        fast = fast->link->link;
        if (fast == slow) {
            return 1;
        }
    }
    return 0;
}

int main()
{
    // insertAtBeginSingle(2);
    // insertAtBeginSingle(12);
    // insertAtBeginSingle(23);
    // insertAtBeginSingle(21);

    insertAtBeginCirc(3);
    insertAtBeginCirc(33);
    insertAtBeginCirc(34);
    insertAtBeginCirc(30);

    if(detectCycle()){
        printf("Cycle Detected");
    }
    else{
        printf("Cycle Not Detected");
    }
}