def bubblesort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    print(arr)


if __name__ == "__main__":
    arr = list(map(int,input("Enter Element : ").split()))
    bubblesort(arr)
