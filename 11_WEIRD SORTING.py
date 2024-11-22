# Sorting : There are two types of sorting 
#           1. Adaptive : which is undertand is the array fully sorted? or half sorted ? and according to this descition is work
#           2. Non Adaptive
# Checking if an array is Soeted of not
def is_sorted(arr):
    sorted = True
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            sorted=False
    return sorted

arr = [1,2, 3, 4, 5, 6, 7]
result = is_sorted(arr)
# This meaning the main topic of this perpose to execution


# Monkey sort
import random
a = [1,2,3,4]
random.shuffle(a)
print(a)

def monkey_sort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)
        print(arr)
    print(arr)

y = monkey_sort([45, 23, 54, 12, 76])
print(y)

# Time complexity : O(infinite)
# sleep sort () its a joke 

