"""Write a python program to store first year percentage of students in array. Write function 
for sorting array of floating point numbers in ascending order using quick sort and display 
top five scores"""
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)

array=[10,9,7,8,4,6,2]

N = len(array)
quicksort(array, 0, N - 1)

print('Sorted array:')
for x in array:    
    print(x, end=" ")

              
        

