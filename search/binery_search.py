def binary_search(array,item,left,right):
    #if left index is greater than right index, then wrong input, return 0
    if(left > right):
        return -1

    #find the middle index
    middle = left + (right-left) // 2
    print("Middle index is ", middle)

    if(array[middle] == item):
        return middle

    elif(array[middle] < item):
        #search the right sub array
        print("Searching in the right sub-array")
        return binary_search(array,item,middle+1,right)

    elif(array[middle] > item):
        #search left sub array
        print("Searching left sub-array")
        return binary_search(array,item,left,middle-1)

if __name__ == "__main__":
    array = [1, 6, 9, 11, 13, 16, 18, 21, 27, 29, 27, 42, 56, 68]
    print(binary_search(array,21,0,len(array)-1))