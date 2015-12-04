import sys


def MaximumSubarray(array):
    """
    Maximum subarray sum calculated using Kadane's algorithm
    """
    max_non_contigious_sum = max_so_far = max_ending_here = 0
    for value in array:
        if value > 0:
            max_non_contigious_sum += value

        max_ending_here = max(0, max_ending_here + value)
        max_so_far = max(max_so_far, max_ending_here)
        return max_so_far, max_non_contigious_sum


if __name__ == '__main__':
    testcases = int(sys.stdin.readline())

    for testcase in range(0, testcases):
        size = int(sys.stdin.readline())
        array = [int(num) for num in sys.stdin.readline().split()]
        max_subarray, max_non_contigious_sum = MaximumSubarray(array)
        print("%s %s" % (max_subarray, max_non_contigious_sum))
