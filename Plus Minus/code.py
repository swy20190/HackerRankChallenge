def plusMinus(arr):
    # Write your code here
    pos_cnt = 0
    neg_cnt = 0
    zero_cnt = 0
    answer = []
    for num in arr:
        if num > 0:
            pos_cnt += 1
        elif num == 0:
            zero_cnt += 1
        else:
            neg_cnt += 1
    print(format(pos_cnt * 1.0 / len(arr), '.6f'))
    print(format(neg_cnt * 1.0 / len(arr), '.6f'))
    print(format(zero_cnt * 1.0 / len(arr), '.6f'))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
