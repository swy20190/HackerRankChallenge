import os


def sockMerchant(n, ar):
    # Write your code here
    answer = 0
    buckets = []
    for i in range(100):
        buckets.append(0)
    for color in ar:
        buckets[color-1]+=1
    for i in range(100):
        answer += int(buckets[i]/2)
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
