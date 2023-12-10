"""Write a python program to store second year percentage of students in array. Write 
function for sorting array of floating point numbers in ascending order using 
a) Insertion sort 
b) Shell Sort and display top five scores"""
def insertionSort(arr):
    n = len(arr) 
    if n <= 1:
        return  
    for i in range(1, n): 
        key = arr[i]  
        j = i-1
        while j >= 0 and key < arr[j]: 
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = key

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

if __name__ == "__main__":
    # Input the number of students
    n = int(input("Enter the number of students: "))

    # Input the second year percentages
    percentages = [float(input(f"Enter percentage for student {i + 1}: ")) for i in range(n)]

    # Sorting using Insertion Sort
    insertion_sort_percentages = percentages.copy()
    insertion_sort(insertion_sort_percentages)

    print("\nTop five scores after Insertion Sort:")
    print(insertion_sort_percentages[-5:][::-1])

    # Sorting using Shell Sort
    shell_sort_percentages = percentages.copy()
    shell_sort(shell_sort_percentages)

    print("\nTop five scores after Shell Sort:")
    print(shell_sort_percentages[-5:][::-1])
