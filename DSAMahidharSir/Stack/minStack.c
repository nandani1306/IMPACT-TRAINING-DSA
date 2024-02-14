#include<stdio.h>

int normalStack[20];
int normalTop=-1;

int minStack[20];
int minTop=-1;


//normal stack operation
void normalpush(int val){
    normalStack[++normalTop]=val;
}

int normalpop(){
    if(normalTop==-1){
        return -1;
    }
    else{
        return normalStack[normalTop--];
    }
}

int normalpeek(){
    if(normalTop==-1){
        return -1;
    }
    else{
        return normalStack[normalTop];
    }
}


//min stack operation
void minpush(int val){
    minStack[++minTop]=val;
}

int minpop(){
    if(minTop==-1){
        return -1;
    }
    else{
        return minStack[minTop--];
    }
}

int minpeek(){
    if(minTop==-1){
        return -1;
    }
    else{
        return minStack[minTop];
    }
}

int main(){
    int val,choice;
    do
    {
        printf("1]push  2]pop   3]peek  4]print 5]exit");
        printf("\nEnter choice:");
        scanf("%d",&choice);

        switch (choice)
        {
        case 1: 
            printf("\nEnter value :");
            scanf("%d",&val);
            normalpush(val);
            if(minTop==-1){
                minpush(val);
            }
            else if (val<=minpeek())
            {
                minpush(val);
            }
            else{
                minpush(minpeek());
            }
            break;
        case 2:
            normalpop();
            minpop();
            break;
        case 3:
            printf("%d",normalpeek());
            break;           
        case 4:
            printf("\nminimum is %d\n",minpeek());
            break;
        case 5:
            break;
        
        }
    } while (choice!=5);
    return 0;
}