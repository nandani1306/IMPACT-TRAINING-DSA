def bs(arr,start,end,target):
    if start<=end:
        mid = (start+end)//2

        if(target == arr[mid]):
            return mid
        elif(target>arr[mid]):
            return bs(arr,mid+1,end,target)
        else:
            return bs(arr,start,end-1,target)
    

if __name__ == "__main__":
    # n = int(input("Enter size:"))
    arr = list(map(int,input("Enter Element").split()))
    target = int(input("Enter target:"))
    print(bs(arr,0,len(arr)-1,target))
    