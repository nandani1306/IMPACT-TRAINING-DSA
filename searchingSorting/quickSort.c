#include<stdio.h>

int partition(int arr[], int start, int end){
    int pivot = arr[start];
    int i = start;
    int j = end;

    while (i<j)
    {
        while(arr[i]<=pivot){
            i++;
        }
        while(arr[j]>pivot){
            j--;
        }
        if(i<j){
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    int temp = arr[start];
    arr[start] = arr[j];
    arr[j] = temp;

    return j;
}

void quicksort(int arr[], int p, int r){
    if(p<r){
        int q = partition(arr, p, r);
        quicksort(arr,p,q-1);
        quicksort(arr,q+1,r);
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
    quicksort(arr,0,n-1);
    printf("Sorted array is:");
    for(int i=0;i<n;i++){
        printf("%d ",arr[i]);
    }
}


