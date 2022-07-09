# implement a merge sort with recursion

items = [6, 20, 9, 19, 34, 23, 41, 29, 52]

def mergesort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]

        # recurively break down the arrays
        mergesort(leftarr)
        mergesort(rightarr)

        # perform the mergin
        i = 0 # index into the left array 
        j = 0 # index into the right array
        k = 0 # index into merged array

        # while both array have content
        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i += 1
            else:
                dataset[k] = rightarr[j]
                j += 1
            k += 1

        # while the left array still has values, add tm
        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i += 1
            k += 1

        # while the right array sitll has values, add them 
        while j < len(rightarr):
            dataset[k] = rightarr[j]
            j += 1
            k += 1

# rest the merge sort with data
print(items)
mergesort(items)
print(items)


