#include<stdio.h>

int bs(int arr[],int start, int end, int target){
    if(start<=end){
        int mid = (start+end)/2;

        if(target == arr[mid]){
            return mid;
        }
        else if (target > arr[mid])
        {
            bs(arr,mid+1,end,target);
        }
        else{
            bs(arr,start,mid-1,target);
        }
    }
    else{
        return -1;
    }
}


int main(){
    int n,target,start,end;
    printf("Enter number of elements:");
    scanf("%d",&n);
    int arr[n];
    printf("Enter Elements:");
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    printf("Enter target :");
    scanf("%d",&target);
    printf("Element is found at %d",bs(arr,0,n-1,target));
}