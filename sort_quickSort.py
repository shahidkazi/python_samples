'''
Sample implementation for Quick Sort Algorithm
'''
def partition (a, start, end):  
    ''' Partition and sort the array iteratively starting with the smallest sized array '''
    i = (start - 1)  
    pivot = a[end] # pivot element  
      
    for j in range(start, end):  
        # If current element is smaller than or equal to the pivot  
        if (a[j] <= pivot):  
            i = i + 1  
            a[i], a[j] = a[j], a[i]  
      
    a[i+1], a[end] = a[end], a[i+1]  
  
    return (i + 1)  


def quick(a, start, end): # a[] = array to be sorted, start = Starting index, end = Ending index      
    ''' Entry function to split and sort the array '''
    if (start < end):  
        p = partition(a, start, end) # p is partitioning index  
        quick(a, start, p - 1)  
        quick(a, p + 1, end)  
  
          
def printArr(a): 
    ''' Function to print the array   '''
    for i in range(len(a)):  
        print (a[i], end = " ")  


''' Driver Code '''
if __name__ == '__main__':
    a = [68, 13, 1, 49, 58]  
    print("Before sorting array elements are - ")  
    printArr(a)  
    quick(a, 0, len(a)-1)  
    print("\nAfter sorting array elements are - ")  
    printArr(a)  
