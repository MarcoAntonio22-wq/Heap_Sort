def heapfy(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[largest] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapfy(arr, n, largest)

def heapsort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapfy(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapfy(arr, i, 0)


arr = [55, 7, 61, 25, 34, 12, 88, 41 , 63]
heapsort(arr)
n = len(arr)
print("valores orgaizados:")
for i in range(n):
    print(arr[i])
