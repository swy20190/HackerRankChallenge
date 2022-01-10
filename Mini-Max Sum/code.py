def miniMaxSum(arr):
    # Write your code here
    min_num = min(arr)
    max_num = max(arr)
    sum_num = sum(arr)
    print(sum_num-max_num, sum_num-min_num)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
