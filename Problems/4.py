"""
Maximum Sum Increasing Subsequence
"""


def maxSumIncreasingSubsequence(arr):
    result = arr.copy()
    for i in range(len(arr)):
        for j in range(i):
            if (arr[j] < arr[i]):
                result[i] = max(result[i], arr[i] + result[j])
    return max(result)

def main():
    arr = [int(x) for x in input().split()]
    print("Maximum sum increasing subsequence : " + str(maxSumIncreasingSubsequence(arr)))

if __name__ == "__main__":
    main()