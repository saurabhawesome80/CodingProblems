"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
"""

def getNewArray(arr):
    productFromRight = [1] * len(arr)
    for i in range(len(arr)-2, -1,-1):
        productFromRight[i] = productFromRight[i+1] * arr[i+1]

    result = []
    productFromLeft = 1
    for i in range(len(arr)):
        result.append(productFromRight[i] * productFromLeft)
        productFromLeft *= arr[i]

    return result


def main():
    arr = [int(x) for x in input().split()]
    print(getNewArray(arr))

if __name__ == "__main__":
    main()