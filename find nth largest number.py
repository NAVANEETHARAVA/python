
Input: 
el = [10,10, 20,30,40, 40]
k = 2
def kthLargest(el, pivotIndex, k):
    pivot = el[pivotIndex]
    lesser = [] #List to store all elements lesser than pivot
    greater = [] #Lsit to store all elements greater than pivot
    equals = [] #List to store all elements equal to pivot

    for x in el:
        if x > pivot:
            greater.append(x)
        elif x < pivot:
            lesser.append(x)
        else:
            equals.append(x)
    g = len(greater) #Length of greater list
    l = len(lesser) 

    if(g == k - 1): #If greater list has k-1 elements, that makes the pivot kth largest element
        return pivot
    elif(g < k):
        return kthLargest(lesser, l - 1, k) #If greater list is smaller than k, kth largest element is in lesser list
    else:
        return kthLargest(greater,  g - 1, k) #Else kth largest element is in greater list
