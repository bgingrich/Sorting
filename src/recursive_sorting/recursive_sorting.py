# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    # Start setting a and b to 0
    x = 0
    y = 0

    # Number = i in range of elements in two arrays
    for i in range(0, elements):
        # If first element of array A is smaller than first element of 
        # B put that element in new array
        if x >= len(arrA):
            merged_arr[i] = arrB[y]
        # Put the rest of numbers after first element of new array
            y += 1
        # Do same for array B
        elif y >= len(arrB):
            merged_arr[i] = arrA[x]
            x += 1
        # Now the same for the actual array
        elif arrA[x] < arrB[y]:
            merged_arr[i] = arrA[x]
            x += 1
        else:
            merged_arr[i] = arrB[y]
            y += 1    
    return merged_arr



# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # Length of array is greater than 1
    if len(arr) > 1:
        # Break lists into 2 arrays
        left = merge_sort(arr[0:int(len(arr)/2)])
        right = merge_sort(arr[int(len(arr)/2):])
        # Merge arrays back together
        arr = merge(left, right)

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
