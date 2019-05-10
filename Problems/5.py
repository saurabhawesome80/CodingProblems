"""
Find Kth Smallest element
"""

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def partition(arr, l, r):
    x,i = arr[r], l
    for j in range(l, r ):
        if arr[j] < x:
            swap(arr, i, j)
            i += 1
    swap(arr, i, r)
    return i

def findKthSmallest(arr, l, r, k):
    if(k > 0 and k <= r+1):
        index = partition(arr, l, r)
        print(arr , l, r, k, index)
        if index+1 == k:
            return arr[index]
        if index+1 > k:
            return findKthSmallest(arr, l, index - 1, k)
        return findKthSmallest(arr, index + 1 , r, k)

def main():
    arr = [int(x) for x in input().split()]
    print("Kth Smallest element in the array is " + str(findKthSmallest(arr, 0, len(arr) - 1, 3)))
    #print(partition([23,12, 42, 64, 78], 0, 4))


if(__name__ == "__main__"):
    main()