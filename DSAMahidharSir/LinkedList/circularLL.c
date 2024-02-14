#include<stdio.h>
#include<stdlib.h>

struct Node
{
    int data;
    struct Node *next;  
};

typedef struct Node Node;

Node* head = NULL;
Node* tail = NULL;

Node *newNode(int value){
    Node *temp = (Node*)malloc(sizeof(Node));
    if (temp==NULL){
        printf("No memory allocated\n");
    }
    temp->data = value;
    temp->next = NULL;
    return temp;
}

//search
Node* search(int value){
    Node *temp = head;
    while (temp!=NULL)
    {
        if(temp->data == value){
            return temp;
        }
        temp=temp->next;
    }
    return NULL; 
}


//insert at begin
void insertAtBegin(int value){
    Node* temp1 = newNode(value);
    if(head == NULL){
        head = temp1;
        head->next = head;
    }
    else{
        Node* temp = head;
        while(temp->next != head)
        {   
            temp = temp->next;
        }
        temp->next = temp1;
        temp1->next = head;
        head = temp1;
    }
}

//insert at end
void insertAtEnd(int value){
    Node* temp1 = newNode(value);
    if(head==NULL){
        head=tail= temp1;
    }
    else{
        Node* temp = head;
        while (temp->next != head)
        {
            temp=temp->next;
        }
        temp1->next = head;
        temp->next = temp1;
    }
}

//insert at any position
void insertAtPos(int prev, int value){
    Node* temp1 = newNode(value);
    if(search(prev)){
        Node* temp = head;
        while (temp->data != prev)
        {
            temp=temp->next;
        }
        temp1->next = temp->next;
        temp->next = temp1;
    }
}

//delete at begin
void deleteAtBegin(){
    if(head==NULL){
        printf("LL is empty");
    }
    else{
        Node* last = head;
        while(last->next != head){
            last=last->next;
        }
        Node* temp = head;
        head = head->next;
        free(temp);
        last->next = head;
    }
}

//delete at end
void deleteAtEnd(){
    if(head==NULL){
        printf("LL is empty");
    }
    else{
        Node* temp = head;
        while (temp->next->next!=head)
        {
            temp=temp->next;
        }
        Node* second = temp->next;
        temp->next=head;
        free(second);
    }
}



//display
void display(){
    if(head == NULL){
        printf("LL is empty");
    }
    else{
        Node* temp = head;
        do 
        {
            printf("%d-> ",temp->data);
            temp = temp->next;
        } while ((temp != head));    
    }
}

int main(){
    insertAtBegin(10);
    insertAtBegin(30);
    insertAtEnd(20);
    insertAtPos(20,100);
    // deleteAtBegin();
    deleteAtEnd();
    display();
}