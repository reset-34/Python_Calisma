def bubble_sort (input_list):
    n = len (input_list)
    for i in range(n-1):
        for j in range (n-i-1):
            if input_list[j]>input_list[j+1]:
                input_list[j],input_list[j+1]=input_list[j+1], input_list[j]
    return input_list


def selection_sort (numbers):
    n = len (numbers)
    for i in range (n):
        min_index =i
        for j in range (i+1,n):
            if numbers[j]<numbers[min_index]:
                min_index=j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers



def insertion_sort(numbers):
     
    for i in range (1,len(numbers)):
        key = numbers[i]
        j= i-1
    
        while j>=0 and numbers [j]<key:
            numbers[j+1]=numbers[j]
            j-=1
        numbers[j+1]=key
    return numbers    