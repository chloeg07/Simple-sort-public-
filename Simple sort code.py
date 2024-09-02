def simple_sort(arr):
    n = len(arr)
#Traverse through all elements in the list
    for i in range(n):
#Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
#Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

if __name__ == "__main__":
#Get user input as a string and split into a list of strings
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
    
    print("Unsorted array:", arr)
    
    simple_sort(arr)
    
    print("Sorted array:", arr)
    
    
    

        
        
        