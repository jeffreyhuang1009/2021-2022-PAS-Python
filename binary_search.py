import time
def binary_search(arr, x):
    start_time=time.time()
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            print("--- %s seconds ---" % (time.time() - start_time))
            return mid
    return -1

list=[0,1,2,3,4,5,6,7,8,9]
print(binary_search(list, 9))