import os


def pickingNumbers(a):
    # Write your code here
    buckets = []
    for i in range(100):
        buckets.append(0)
    for num in a:
        buckets[num] += 1
    answer = -1
    for i in range(99):
        answer = max(answer, buckets[i]+buckets[i+1])
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
