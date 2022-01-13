import os


def migratoryBirds(arr):
    # Write your code here
    buckets = []
    for i in range(5):
        buckets.append(0)
    for t in arr:
        buckets[t - 1] += 1
    answer = 0
    max_f = -1
    for i in range(5):
        if buckets[i] > max_f:
            max_f = buckets[i]
            answer = i + 1

    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()