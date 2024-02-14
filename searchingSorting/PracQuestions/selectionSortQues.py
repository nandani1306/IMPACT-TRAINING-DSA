def selection(arr):
    n=len(arr)
    for i in range(n-1,0,-1):
        max=i
        for j in range(i-1,-1,-1):
            if arr[max]<=arr[j]:
                max=j
        if(i!=max):
            temp=arr[max]
            arr[max]=arr[i]
            arr[i]=temp    
        print(" ",max)    
        
    return arr            
            
if __name__=="__main__":
    inp=list(map(int,input("Enter the Elements : ").split()))
    ans=selection(inp)
    # print(ans)