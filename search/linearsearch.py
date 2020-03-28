def linear_search(array,item):
    #simple linear search O(N) time complexity
    for i in range(len(array)):
        #If the given item is found, return it's position
        if array[i] == item:
            return i
    #Not found, return item not found
    return -1

if __name__ == "__main__":
    array = [1,3,4,5,6,67,64,7,72,69,43]
    print(linear_search(array,4))