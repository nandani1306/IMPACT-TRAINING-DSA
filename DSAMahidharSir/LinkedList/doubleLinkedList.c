#include<stdio.h>
#include<stdlib.h>

struct Node
{
    struct Node *prev;
    int data;
    struct Node *next;  
};

typedef struct Node Node;

Node *head = NULL;
Node *tail = NULL;

Node *newNode(int value){
    Node *temp = (Node*)malloc(sizeof(Node));
    if (temp==NULL){
        printf("No memory allocated\n");
    }
    temp->prev = NULL;
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
int insertAtBegin(int value){
    Node *temp1 = newNode(value);
    if(head==NULL){
        head = temp1;
    }
    else{
        temp1->next = head;
        head->prev = temp1;
        head = temp1;
    }
}

//insert at end
void insertAtEnd(int value){
    Node *temp1 = newNode(value);
    if(head == NULL){
        head = tail = temp1;
    }
    else{
        Node *temp = head;
        while (temp->next!=NULL)
        {
            temp = temp->next;
        }
        temp->next = temp1;
        temp1->prev = temp;
        tail = temp1;
    }
}

//insert after
void insertAfter(int prev, int value){
    Node* temp1 = newNode(value);

    if(search(prev)){
        Node* temp = head;
        while (temp->data != prev)
        {
            temp = temp->next;
        }
        temp1->next = temp->next;
        temp1->prev = temp;
        temp->next = temp1;
        temp1->next->prev = temp1;
    }
}

//display
void display(){
    if(head == NULL){
        printf("LL is empty");
    }
    else{
        Node* temp = head;
        while (temp != NULL)
        {
            printf("%d-> ",temp->data);
            temp = temp->next;
        } 
    }
}

//delete at begin
void deleteAtBegin(){
    if(head==NULL){
        printf("LL is empty");
    }
    else{
        Node* temp = head;
        head = head->next;
        free(temp);
    }
}

//delete at end
void deleteAtEnd(){
    if(head == NULL){
        printf("LL is empty");
    }
    else{
        Node* temp = head;
        while (temp->next->next != NULL)
        {
            temp = temp->next;
        }
        Node* tempp = temp->next;
        temp->next = NULL;
        free(tempp);
    }
}

//delete at any position
void deleteAtPos(int prev){
    if(search(prev)){
        Node* temp = head;
        while (temp->next->data != prev)
        {
            temp = temp->next;
        }
        Node* tempp = temp->next;
        temp->next = tempp->next;
        tempp->next->prev = temp;
        free(tempp);
    }
}



int main(){
    // insertAtBegin(10);
    // insertAtBegin(12);
    // insertAtBegin(13);
    // insertAtEnd(14);
    // insertAfter(12,11);
    // // deleteAtEnd();
    // // deleteAtEnd();
    // deleteAtPos(11);
    // display();
    int ch,value,target,prev;
    while(ch!=9){
        printf("\n 1]Insert at Begin\n 2]Insert at Middle\n 3]Insert at End\n 4]Delete at Begin\n 5]Delete at Middle\n 6]Delete at End\n 7]Search\n 8]Display\n 9]Exit\n");
        printf("Enter your Choice:\n");
        scanf("%d",&ch);

        switch (ch)
        {
        case 1:
            printf("Enter value to insert:");
            scanf("%d",&value);
            insertAtBegin(value);
            break;
        case 2:
            printf("Enter value after which you want to insert:");
            scanf("%d",&prev);
            printf("Enter value to insert:");
            scanf("%d",&value);
            insertAfter(prev,value);
            break;
        case 3:
            printf("Enter value to insert:");
            scanf("%d",&value);
            insertAtEnd(value);
            break;
        case 4:
            deleteAtBegin();
            break;
        case 5:
            printf("Enter prev value to delete:");
            scanf("%d",&value);
            deleteAtPos(value);
            break;
        case 6:
            deleteAtEnd();
            break;
        case 7:
            printf("Enter value to search:");
            scanf("%d",&target);
            if(search(target)){
                printf("%d Present",target);
            }
            else{
                printf("%d Absent",target);
            }
            break;
        case 8:
            display();
        case 9:
            break;
        default:
            break;
        }
    }
}
