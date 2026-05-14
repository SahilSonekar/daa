## Selection Sort 

# def selectionSort(arr):
#     n = len(arr)

#     for i in range(n):
#         idx = i
#         for j in range(i+1, n):
#             if arr[idx] > arr[j]:
#                 idx = j

#         arr[idx], arr[i] = arr[i], arr[idx]

#     return arr

# print(selectionSort([12, 25, 29, 8, 32, 17, 40]))





## Recursion Selection Sort 

# def recSelectionSort(arr, i, n):
#     if i >= n-1:
#         return
    
#     idx = i
#     for j in range(i+1, n):
#         if arr[idx] > arr[j]:
#             idx = j

#     arr[idx], arr[i] = arr[i], arr[idx]

#     recSelectionSort(arr, i+1, n)
#     return arr

# arr = [12, 25, 29, 8, 32, 17, 40]
# print(recSelectionSort(arr,0,len(arr)))




## Insertion Sort

# def insertionSort(arr):
#     n = len(arr)

#     for i in range(1,n):
#         j = i

#         while j > 0 and arr[j-1] > arr[j]:
#             arr[j-1], arr[j] = arr[j], arr[j-1]
#             j -= 1

#     return arr

# print(insertionSort([12, 25, 29, 8, 32, 17, 40]))



## Recursion Insertion sort

# def recInsertionSort(arr, i):
#     n = len(arr)
#     if i >= n-1:
#         return
    
#     j = i
#     while j > 0 and arr[j-1] > arr[j]:
#         arr[j-1], arr[j] = arr[j], arr[j-1]
#         j -= 1

#     recInsertionSort(arr, i+1)
#     return arr

# print(recInsertionSort([12, 25, 29, 8, 32, 17, 40], 1))
    





# def bubbleSort(arr):
#     n = len(arr)

#     for i in range(n):
#         swap = False

#         for j in range(1,n-i):
#             if arr[j] < arr[j-1]:
#                 arr[j], arr[j-1] = arr[j-1], arr[j]
#                 swap = True
#             print(arr)

#         if not swap:
#             break

#     return arr

# print(bubbleSort([12, 25, 29, 8, 40, 32, 17]))





## Recursion bubble sort

# def recBubbleSort(arr, i):
#     n = len(arr)
#     swap = False
#     if i >= n:
#         return

#     for j in range(1,n-i):
#         if arr[j-1] > arr[j]:
#             arr[j-1], arr[j] = arr[j], arr[j-1]
#             swap = True

#     if not swap:
#         return arr
    
#     recBubbleSort(arr, i+1)
#     return arr
    
# print(recBubbleSort([12, 25, 29, 8, 40, 32, 17], 0))






## Merge sort

# def merge(arr, low, mid, high):
#     temp = []
#     left = low
#     right = mid + 1

#     while left<=mid and right<=high:
#         if arr[left] <= arr[right]:
#             temp.append(arr[left])
#             left += 1
#         else:
#             temp.append(arr[right])
#             right += 1

#     while left <= mid:
#             temp.append(arr[left])
#             left += 1

#     while right <= high:
#             temp.append(arr[right])
#             right += 1  

#     for i in range(low, high+1):
#         arr[i] = temp[i - low]

# def mergeSort(arr, low, high):
#     if low >= high:
#         return
    
#     mid = (low+high)//2

#     mergeSort(arr, low, mid)
#     mergeSort(arr, mid+1, high)
#     merge(arr, low, mid, high)

#     return arr

# arr = [45, 12, 89, 33, 77, 23, 9, 51, 60, 19, 40]
# print(mergeSort(arr, 0, len(arr)-1))





## Quick sort

# def partition(arr, low, high):
#     pivot = arr[low]
#     i = low
#     j = high

#     while i < j:
#         while arr[i] <= pivot and i <= high-1:
#             i += 1

#         while arr[j] >= pivot and j >= low+1:
#             j -= 1

#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]

#         print(arr)

#     arr[low], arr[j] = arr[j], arr[low]
#     print(arr)
#     return j

# def quickSort(arr, low, high):
#     if low < high:
#         pindex = partition(arr, low, high)
#         quickSort(arr, low, pindex-1)
#         quickSort(arr, pindex+1, high)

#     return arr

# arr = [43, 32, 22, 78, 63, 57, 91, 13]
# quickSort(arr, 0, len(arr)-1)






