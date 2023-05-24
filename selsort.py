def selsort(arr):

    n = len(arr)
    print("\nList before Sorting:", arr)   #print unsorted array list

    for i in range(n):
        min_idx = i   #index of unsorted element

        for j in range(i + 1, n):   #to compare with remaining elements
            if arr[j] < arr[min_idx]:   #checks current element at j < assumed min element
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]   #to swap 1st element with 1st remaing unsorted
        print("List After Pass", i + 1, ":", arr)     #to display array after each sort
    return arr

n = int(input("Length of List: "))
arr = []

for i in range(n):
    element = int(input("Enter List Element: "))
    arr.append(element)

print("\nSorted List is:", selsort(arr))
