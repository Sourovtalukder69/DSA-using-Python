# Merge sort 
#  [1, 2,3, 4]   [5, 6, 7, 8]
# worst case time complexity n(logn)
# space complexity : 
def merge_sorted(arr1, arr2):
    merge = []
    i = j = 0
    while i < len(arr1) and j< len(arr2):
        if arr1[i] < arr2[j]:
            merge.append(arr1[i])
            i = i + 1
        else:
            merge.append(arr2[j])
            j = j+1
    while i < len(arr1):
        merge.append(arr1[i])
        i = i+1

    while j < len(arr2):
        merge.append(arr2[j])
        j = j + 1

    return merge
   

arr1 = [1, 2, 4]
arr2 = [3, 5, 7, 8, 9]
result = merge_sorted(arr1, arr2)
print(result)


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    left = merge_sort(left)
    right = merge_sort(right)
    return merge_sorted(left, right)




# Updated marge sort algorithms
def merge_sorted(arr1, arr2, arr):
    i = j = k = 0
    while i < len(arr1) and j< len(arr2):
        if arr1[i] < arr2[j]:
            merge.append(arr1[i])
            arr[k] = arr1[i]
            i = i + 1
        else:
            merge.append(arr2[j])
            arr[k] = arr2[j]
            j = j+1
        k = k + 1
    while i < len(arr1):
        merge.append(arr1[i])
        arr[k] = arr1[i]
        i = i+1

    while j < len(arr2):
        merge.append(arr2[j])
        j = j + 1

    return merge
   

arr1 = [1, 2, 4]
arr2 = [3, 5, 7, 8, 9]
result = merge_sorted(arr1, arr2)
print(result)


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    left = merge_sort(left)
    right = merge_sort(right)
    return merge_sorted(left, right)


