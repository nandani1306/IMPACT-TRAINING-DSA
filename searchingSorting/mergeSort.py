def merge(arr,l,m,r):
    n1 = m-l+1 
    n2 = r-m
    L=[0]*n1 
    R=[0]*n2 
    # L[n1],R[n2]

    for i in range(n1):
        L[i] = arr[l+i]

    for j in range(n2):
        R[j] = arr[m+1+j]
    i=0
    j=0
    k=l
    while(i<n1 and j<n2):
        if(L[i] <= R[j]):
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergesort(arr,l,r):
    if l < r:
        m = (l+r)//2
        mergesort(arr,l,m)
        mergesort(arr,m+1,r)
        merge(arr,l,m,r)

if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = []
    print("Enter Elements:")
    for i in range(n):
        arr.append(int(input()))

    mergesort(arr, 0, n-1)

    print("Sorted array is:", end=" ")
    for i in range(n):
        print(arr[i], end=" ")