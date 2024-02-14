#include<stdio.h>
#define SIZE 5

int stack[SIZE];
int top=-1;
int ch;
int val;

void push(int val){
    if(top==SIZE-1){
        printf("\nStack OverFlow");
    }
    else{
        top+=1;
        stack[top]=val;
    }
}

void pop(){
    if(top==-1){
        printf("\nStack is Empty");
    }
    else{
        printf("\nElement popped:%d",stack[top]);
        top-=1;
    }
}

void peek(){
    if(top==-1){
        printf("Stack is Empty Nothing to show");
    }
    else{
    printf("\nElement at top is:%d",stack[top]);
    }
}

void printStack(){
    for(int i=0;i<=top;i++){
        printf("%d\t",stack[i]);
    }
}

int main(){
    do{
    printf("\nEnter your choice:");
    printf("\n1.Push\t2.Pop\t3.Peek\t4.Print\t5.Exit\n");
    scanf("%d",&ch);
        switch (ch)
        {
        case 1:
            printf("Enter element to push:");
            scanf("%d",&val);
            push(val);
            break;
        case 2:
            pop();
            break;
        case 3:
            peek();
            break;
        case 4:
            printStack();
            break;
        case 5:
            break;
        }
    }while(ch!=5);
    return 0;
}