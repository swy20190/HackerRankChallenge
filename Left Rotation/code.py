import os


def rotateLeft(d, arr):
    # Write your code here
    n = len(arr)
    abs_d = d%n
    answer = []
    for i in range(abs_d, n):
        answer.append(arr[i])
    for i in range(abs_d):
        answer.append(arr[i])
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')