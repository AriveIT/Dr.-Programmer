# get nmq input
nmq = list(map(int, input().split(" ")))
xCoords = list(map(int, input().split(" ")))
yCoords = list(map(int, input().split(" ")))
xCoords.sort()
yCoords.sort()

# binary search, recursive
def binary_search(arr, low, high, x):
 
    # Check base case
    if high > low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        # Return index closest to value
        return high

def countSolutions(xList, yList, z):
    counter = 0

    for x in xList:
        for y in yList:
            if(y + x < z):
                counter += 1
    
    return counter

def queryA (z, l1, r1):
    l1Index = binary_search(xCoords, 0, len(xCoords), l1)
    r1Index = binary_search(xCoords, 0, len(xCoords), r1)

    # correct indexes
    if(xCoords[l1Index] < l1):
        l1Index += 1
    elif(xCoords[r1Index] > r1):
        r1Index -= 1

    # determine number of possible combinations
    return countSolutions(xCoords[l1Index: r1Index + 1], yCoords, z)

def queryB (z, l2, r2):
    l2Index = binary_search(yCoords, 0, len(yCoords), l2)
    r2Index = binary_search(yCoords, 0, len(yCoords), r2)

    # correct indexes
    if(yCoords[l2Index] < l2):
        l2Index += 1
    elif(yCoords[r2Index] > r2):
        r2Index -= 1

    # determine number of possible combinations
    return countSolutions(xCoords, yCoords[l2Index: r2Index + 1], z)

def queryC (z, l1, r1, l2, r2):
    l1Index = binary_search(xCoords, 0, len(xCoords), l1)
    r1Index = binary_search(xCoords, 0, len(xCoords), r1)
    l2Index = binary_search(yCoords, 0, len(yCoords), l2)
    r2Index = binary_search(yCoords, 0, len(yCoords), r2)

    # correct indexes
    if(xCoords[l1Index] < l1):
        l1Index += 1
    elif(xCoords[r1Index] > r1):
        r1Index -= 1
    if(xCoords[l1Index] < l1):
        l1Index += 1
    elif(xCoords[r1Index] > r1):
        r1Index -= 1

    return countSolutions(xCoords[l1Index: r1Index + 1], yCoords[l2Index: r2Index + 1], z)



# get queries input
queries = []

for x in range(nmq[2]):
    queries.append(input())

for x in range(nmq[2]):
    current = queries[x].split(" ")

    if(current[1] == "A"):
        print(queryA(int(current[0]), int(current[2]), int(current[3])))
    elif(current[1] == "B"):
        print(queryB(int(current[0]), int(current[2]), int(current[3])))
    elif(current[1] == "C"):
        print(queryC(int(current[0]), int(current[2]), int(current[3]), int(current[4]), int(current[5])))









