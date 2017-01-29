# Quicksort algorithm
# GJM

# Quicksort algorithm involves 2 high-level steps (not in-place variant)
# Step 1: choose a pivot element in list ('first', 'last', or 'mo3'(median-of-three)) and swap with 1st element of list
# Step 2: sort all elements lower than pivot to left of pivot and all greater to right of pivot, recurse on each subarry

def quickSort(subarr, arrlen, pivot_type):
    #base case
    if arrlen <= 1:
        return subarr

    p = choosePivot(subarr, arrlen, pivot_type)

    #partition subarr around "p"
    i = 1       #delineates boundary of whats less than and whats greater than.  Increment after swap
    j = 1       #counter; increment after every subarr comparison (keeps track of what we looked at and what we haven't)
    for ind in range(1, len(subarr)):
        if subarr[j] > p:
            #leave in place
            j+=1
        else:
            #smaller values on left of pivot: swap
            temp = subarr[i]
            subarr[i] = subarr[j]
            subarr[j] = temp
            i+=1
            j+=1
    #swap the pivot into the empty entry (delineated boundary "i")
    temp = subarr[0]
    subarr[0] = subarr[i-1]
    subarr[i-1] = temp

    #recurse on both subarrays
    subarr1 = quickSort(subarr[0:i-1], len(subarr[0:i-1]), pivot_type)
    subarr2 = quickSort(subarr[i:len(subarr)], len(subarr[i:len(subarr)]), pivot_type)
    return subarr1+[p]+subarr2

def choosePivot(arr, array_len, piv_type):
    #choose first entry as pivot
    if piv_type == 'first':
        return arr[0]
    #choose last element as pivot
    if piv_type == 'last':
        #swap first and last element, then return first element (previously last element)
        temp = arr[0]
        arr[0] = arr[array_len-1]
        arr[array_len-1] = temp
        return arr[0]
    #choose median-of-three
    if piv_type == 'mo3':
        pivot_lst = list()
        pivot_lst.append(arr[0])                #first
        if array_len%2 == 0:                    #middle
            #even
            pivot_lst.append(arr[array_len/2 - 1])
        else:
            #odd
            pivot_lst.append(arr[array_len / 2])
        pivot_lst.append(arr[array_len - 1])    #last
        unsort_piv_lst = list()
        for i in pivot_lst:
            unsort_piv_lst.append(i)

        pivot_lst.sort()

        #find median of set containing first, middle, and last element
        median = pivot_lst[1]

        #swap median with 1st element
        temp = arr[0]
        arr[0] = median
        ind = unsort_piv_lst.index(median)
        if ind == 0:
            arr[0] = temp
        elif ind == 1:
            if array_len%2 == 0:
                arr[array_len / 2 - 1] = temp
            else:
                arr[array_len / 2] = temp
        else:
            arr[array_len - 1] = temp
        return arr[0]

with open('10') as f:
    arr = f.readlines()
arr = map(int, arr)
pivot_type = 'mo3'   # median of three pivot

sort_arr = quickSort(arr, len(arr), pivot_type)
a = 1
