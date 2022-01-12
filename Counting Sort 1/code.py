import os


def countingSort(arr):
    # Write your code here
    answer = []
    for i in range(100):
        answer.append(0)
    for num in arr:
        answer[num] += 1
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
