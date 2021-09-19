def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):  
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
  


arr = []
print("size: ")
n=int(input())
print("enter list")
for i in range (n):
    arr.append(int(input()))
bubbleSort(arr)
print(sorted)
for i in range(len(arr)):
    print ("%d" %arr[i])

