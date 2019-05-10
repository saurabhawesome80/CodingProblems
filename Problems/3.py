"""
Find maximum sum subarray - Kadene's Algorithm
"""

def findMaximumSumSubArray(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    for i in range(1,len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(current_sum, max_sum)
    return max_sum


def main():
    arr = [int(x) for x in input().split()]
    print("Maximum sum subarray is " + str(findMaximumSumSubArray(arr)))

if __name__ == "__main__":
    main()