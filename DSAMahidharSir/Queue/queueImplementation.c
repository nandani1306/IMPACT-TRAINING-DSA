#include<stdio.h>
#define n 5
int queue[n];
int front=-1,rear=-1;

void enque(int val){
    if(rear==n-1){
        printf("\nQueue Over");
    }
        rear++;
        queue[rear]=val;
    if(rear==0){
        front=0;
    }
}

int dequeue(){
    if(front==-1 && rear==-1){
        printf("\nQueue Underflow");
    }
    else if(front != rear){
        front++;
    }
    else if(front==rear){
        front=-1;
        rear=-1;
    }
    
}

void display(){
    if(front==rear && (front==-1&&rear==-1)){
        printf("\nQueue empty");
    }
    else{
        for(int i=front;i<=rear;i++){
            printf("\n%d  ",queue[i]);
        }
    }
}

int main(){
    int val;
    int ch;
     do{
        printf("\n1.Enque 2.Dequeue 3.Print 4.Exit");
        printf("\nEnter your choice:");
        scanf("%d",&ch);
        switch (ch)
        {
        case 1:
            printf("\nEnter element to push:");
            scanf("%d",&val);
            enque(val);
            break;
        case 2:
            dequeue();
            break;
        case 3:
            display();
            break;
        case 4:
            break;
        default:
            break;
        }
    }while(ch!=4);

    return 0;
}