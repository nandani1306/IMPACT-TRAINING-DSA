def selectionsort(arr):
    n=len(arr)
    for i in range(n):
        min = i 
        for j in range(i+1, n):
            if arr[j]<arr[min]:
                min = j 
            
        if min != i:
            temp = arr[i]
            arr[i] = arr[min]
            arr[min] = temp
    print(arr)


if __name__ == "__main__":
    arr = list(map(int,input("Enter Element : ").split()))
    selectionsort(arr)
