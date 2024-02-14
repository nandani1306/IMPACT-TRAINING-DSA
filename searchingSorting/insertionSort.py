def insertionsort(arr):
    n = len(arr)
    for i in range(n):
        temp = arr[i]
        j = i-1 

        while(j>=0 and temp<=arr[j]):
            arr[j+1] = arr[j]
            j = j-1

        arr[j+1] = temp
    print(arr)

if __name__ == "__main__":
    arr = list(map(int,input("Enter Element : ").split()))
    insertionsort(arr)