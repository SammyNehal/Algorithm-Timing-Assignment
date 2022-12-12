import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


trials = int(input('Enter the number of trials: '))
size = int(input('Enter the size of the dataset: '))

# Create an empty list to store the times for each trial
bubble_sort_times = []
quick_sort_times = []
built_in_sort_times = []


for i in range(trials):
    # Generate a random list of integers
    arr = [random.randint(0, 1000) for i in range(size)]
    
    # Measure the time it takes to sort the list using bubble sort
    start = time.time()
    bubble_sort(arr)
    end = time.time()
    bubble_sort_times.append(end - start)
    
    # Measure the time it takes to sort the list using quick sort
    arr = [random.randint(0, 100) for i in range(size)]
    start = time.time()
    quick_sort(arr, 0, len(arr)-1)
    end = time.time()
    quick_sort_times.append(end - start)
    
    # Measure the time it takes to sort the list using the built-in sort function
    arr = [random.randint(0, 100) for i in range(size)]
    start = time.time()
    arr.sort()
    end = time.time()
    built_in_sort_times.append(end - start)



bubble_sort_avg = sum(bubble_sort_times) / len(bubble_sort_times)
quick_sort_avg = sum(quick_sort_times) / len(quick_sort_times)
built_in_sort_avg = sum(built_in_sort_times) / len(built_in_sort_times)
  
print('\033[31mBubble sort times:', bubble_sort_times)
print('\033[31mQuick sort times:', quick_sort_times)
print('\033[31mBuilt-in sort times:', built_in_sort_times)


print('\033[32mTotal time for Bubble sort:', sum(bubble_sort_times))
print('\033[32mTotal time for Quick sort:', sum(quick_sort_times))
print('\033[32mTotal time for Built-in sort:', sum(built_in_sort_times))



print('\033[34mAverage time for Bubble sort:', bubble_sort_avg)
print('\033[34mAverage time for Quick sort:', quick_sort_avg)
print('\033[34mAverage time for Built-in sort:', built_in_sort_avg)