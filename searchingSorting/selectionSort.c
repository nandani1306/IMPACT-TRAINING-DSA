#include<stdio.h>

void selectionsort(int arr[],int n){
    for (int i = 0; i < n; i++)
    {
        int min = i;
        for(int j = i+1;j<n;j++){
            if(arr[j] < arr[min]){
                min = j;
            }

            if(min!=i){
                int temp = arr[i];
                arr[i] = arr[min];
                arr[min] = temp;
            }
        }
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
    selectionsort(arr,n);
    printf("Sorted array is:");
    for(int i=0;i<n;i++){
        printf("%d ",arr[i]);
    }
}