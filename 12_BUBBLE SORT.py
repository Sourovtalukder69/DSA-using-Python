# Bubble Sort  Algorithms


# Inputs: 1.Array = [4, 6, 2, 1, 3, 8]
# output : sorted array = [1, 2, 4, 6, 8]
# Bubble sort is stable
# N numer of item = (N-1) number of pass
# Number of comparism = (N-1) + (N-2)+ (N-3) + (N-4)+ (N-n).....

def bubble_sort(arr):
    for i in range(len(arr)-1):  # for passes
        for j in range(len(arr) -1 -i): # for compare 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]   # a, b = b, a (swaping)

    print(arr)

arr = [23, 12, 34, 11, 100, 56, 78]
result = bubble_sort(arr)
print(result)


# Can i make adapdet of this  algorithms
# Yes !

def bubble_sort(arr):
    for i in range(len(arr)-1):
        flag = 0  # set for adabtive check
        for j in range(len(arr) -1 -i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = 1
        if flag == 0:
            break
               

    print(arr)

# Best case time complexity O(n)

arr = [3, 2, 4, 5, 6]
result = bubble_sort(arr)
print(result)

