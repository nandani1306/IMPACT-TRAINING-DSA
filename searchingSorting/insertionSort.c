#include<stdio.h>

void insertionsort(int arr[], int n){
    int i,j,temp;
    for(int i=1; i<n; i++){
        temp = arr[i];
        j=i-1;

        while (j>=0 && temp<=arr[j])
        {
            arr[j+1] = arr[j];
            j=j-1;
        }
        arr[j+1] = temp;
    }
}

int main(){
    int n;
    printf("Enter number of elements:");
    scanf("%d",&n);
    int arr[n];
    printf("Enter Elements:");
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    insertionsort(arr,n);
    printf("Sorted array is:");
    for(int i=0;i<n;i++){
        printf("%d ",arr[i]);
    }
}