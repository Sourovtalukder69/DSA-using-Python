# Selection Sort


#          i -->
# array = [8, 9, 1, 3, 7]
#         min j

#             i -->
# array = [1, 9, 8, 3, 7]
#                j

#                i
# array = [1, 3, 8, 9, 7]
#                   j

# and finally for 5 item i use 4 pass : n item = (n-1) pass
# array = [1, 3, 7, 8, 9]


def selection_sort(arr):
    for i in range(len(arr)- 1):  #  n item = (n-1) pass
        print(i+1, 'pass', end="")
        min = i
        print("curr min is", arr[min])
        for j in range(i+i, len(arr)):
            print("current item under obserbation ", arr[j])
            if arr[j]< arr[min]:
                print("curr item is less than min")
                min = j
                print("Now the min has become", arr[min])

            arr[i], arr[min] = arr[min], arr[i]
        print(arr)
    
    print(arr)


arr = [8, 9, 1, 3, 7]
result = selection_sort(arr)


# Is selection sort adaptive ? 
# No it is not adaptive . And it can not make adaptive beacuse in this selection sort there is not mechanism to check arry next items sortted or not

# So in worst case Selection sort is better than bubble sort. But in Best case its oposite

# And Selection sort is also not Stable

