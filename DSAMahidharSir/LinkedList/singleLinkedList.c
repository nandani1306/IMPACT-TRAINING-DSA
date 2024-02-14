#include<stdio.h>
#include<stdlib.h>

struct Node
{
    int data;
    struct Node *link;  
};

//nickname for "struct Node " is "Node"
typedef struct Node Node;

// struct Node *head = NULL;   OR
Node *head = NULL;
Node *tail = NULL;


//creating a new node
// struct Node *newNode(int value){     OR
Node *newNode(int value){
    Node *temp = (Node*)malloc(sizeof(Node));
    if (temp == NULL){
        printf("No memory allocated\n");
    }
    temp->data = value;
    temp->link = NULL;
    return temp;
}


//searching
Node* search(int value){
    Node *temp = head;

    while (temp != NULL)
    {
        if(temp->data==value)
            return temp;
        temp = temp->link;
    }
    return NULL;
}


//insertion at begin
int insertAtBegin(int value){
    if(head == NULL){
        head = newNode(value);
    }
    else{
        Node *temp = newNode(value);
        temp->link = head;
        head = temp;
    }
}


//insert at end
void insertAtEnd(int value){
    if(head == NULL){
        head = tail = newNode(value);
    }
    else{
        Node *temp = head;
        while(temp->link != NULL){
            temp=temp->link;
        }
        Node *temp1 = newNode(value);
            temp->link = temp1;
            tail = temp1;
    }
}


//insert after
void insertAfter(int prev,int value){
    // Node currentPosition = search(value);
    Node *temp1 = newNode(value);
    if(search(prev)){
        Node* temp = head;
        while(temp->data != prev){
            temp = temp->link;
        }
        temp1->link = temp->link;
        temp->link = temp1;
        
    }    
}

void display(){
    if(head==NULL){
        printf("No LL to display\n");
    }
    else{
        Node* temp = head;
        while(temp != NULL){
        printf("%d->",temp->data);
        temp = temp->link;
    }
    }
}


//delete at begin
void deleteAtBegin(){
    if(head == NULL){
        printf("LL is Empty\n");
    }
    else{
        Node* temp = head;
        head = head->link;
        free(temp);
    }
}


//delete at end
void deleteAtEnd(){
    if(head == NULL)
        printf("LL is empty\n");
    else{
        Node *temp = head;
        while (temp->link->link != NULL)
        {
            temp = temp->link;
        }
        Node *tempo = temp->link;
        temp->link = NULL;
        free(tempo);
    }
}


//delete at any position
void deleteAfter(int prev){
    if(search(prev)){
        Node *temp = head;
        while (temp->link->data != prev)
        {
            temp = temp->link;
        }
        Node *temp1 = temp->link;
        temp1->link = temp1->link->link;
        free(temp1->link);
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

int main(){
    int ch,value,target,prev;
    while(ch!=11){
        printf("\n 1]Insert at Begin\n 2]Insert at Middle\n 3]Insert at End\n 4]Delete at Begin\n 5]Delete at Middle\n 6]Delete at End\n 7]Detect Cycle\n 8]Search\n 9]Display\n 10]Mid Element\n 11]Exit\n");
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
            deleteAfter(value);
            break;
        case 6:
            deleteAtEnd();
            break;
        case 7:
            if(detectCycle()){
                printf("Cycle Detected\n");
            }
            else{
                printf("Cycle Not Detected\n");
            }
            break;
        case 8:
            printf("Enter value to search:");
            scanf("%d",&target);
            search(target);
            break;
        case 9:
            display();
        case 10:
            printf("Mid element is :%d\n",findMid());
            break;
        case 11:
            break;
        default:
            break;
        }
    }
    
}