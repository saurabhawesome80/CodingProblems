"""
Find first missing positive integer in Linear Time and Constant Time
"""

def swap(arr, i, j):
    arr[i],arr[j] = arr[j],arr[i]

def moveAllNegativeIntToRight(arr):
    #First positive integer from right
    i = len(arr) - 1
    while(i >= 0):
        if arr[i] > 0:
            break
        i -= 1
    
    j = 0
    while(j < i):
        if(arr[j] <= 0):
            swap(arr,i,j)
            i -= 1
        j += 1
    
    return i

def getFirstMissingInteger(arr):
    endIndex = moveAllNegativeIntToRight(arr)
    for i in range(endIndex+1):
        if(abs(arr[i]) - 1 <= endIndex):
            arr[abs(arr[i]) - 1] = -1 * arr[abs(arr[i]) - 1]
            
    for i in range(endIndex + 1):
        if arr[i] > 0:
            return i+1
    return endIndex + 2

def main():
    arr = [int(x) for x in input().split()]
    print(getFirstMissingInteger(arr))

if __name__ == "__main__":
    main()