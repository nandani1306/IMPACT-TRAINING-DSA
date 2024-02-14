def partition(arr,start,end)->int:
    pivot = arr[start]
    i = start
    j = end

    while(i<j):
        while(arr[i]<=pivot):
            i+=1

        while(arr[j]>pivot):
            j-=1

        if i<j:
            arr[i],arr[j] = arr[j],arr[i]

    arr[start],arr[j] = arr[j],arr[start]

    return j
            
def quicksort(arr,p,r):
    if (p<r):
        q = partition(arr,p,r)
        quicksort(arr,p,q-1)
        quicksort(arr,q+1,r)


n = int(input("Enter number of elements: "))
arr = []
print("Enter Elements:")
for i in range(n):
    arr.append(int(input()))

quicksort(arr, 0, n-1)

print("Sorted array is:", end=" ")
for i in range(n):
    print(arr[i], end=" ")

