# Merge Sort algorithm
# sa1: subarray 1
# sa2: subarray 2

def merge_sort(sa1, sa2, res):
    #i and j are counters for each subarray (sa1 and sa2)
    i = 0
    j = 0
    for k in range(0, (len(sa1)+len(sa2))):
        # counter for subarray1 is at the end
        if i == len(sa1):
            while j <= (len(sa2)-1):
                res[k] = sa2[j]
                j+=1
                k+=1
            return {'result': res}
        # counter for subarray2 is at the end
        if j == len(sa2):
            # since subarray2 is at the end already, but "i" has not reached the end of subarray1, keep pushing
            # each element of subarray1 to end of list
            while i <= (len(sa1)-1):
                res[k] = sa1[i]
                i+=1
                k+=1
            return {'result': res}
        # element in subarray2 is larger, must be placed into "res" first
        if sa1[i] > sa2[j]:
            res[k] = sa2[j]
            j+=1
        else:
            res[k] = sa1[i]
            i+=1
    return {'result': res}

def split_subarray(subarray):
    #base case
    if len(subarray) == 1:
        return subarray

    #create 2 empty subarrays used to store each half of subarray
    mid = len(subarray)/2
    sub1 = subarray[0:mid]
    sub2 = subarray[mid:len(subarray)]

    #recursively split arrays until only 1 element left in subarrays (base case)
    res = split_subarray(sub1)
    res = split_subarray(sub2)
    res = merge_sort(sub1, sub2, subarray)

    return

with open('/home/gus/Desktop/Algos/01_merge_sort/unsorted_shortlist_int.txt') as f:
    grades = f.readlines()
grades = map(int, grades)
res = split_subarray(grades)
print(res)