import os


def maximumPerimeterTriangle(sticks):
    # Write your code here
    n = len(sticks)
    sticks.sort()
    sticks.reverse()
    for i in range(n - 2):
        if sticks[i + 1] + sticks[i + 2] > sticks[i]:
            return [sticks[i + 2], sticks[i + 1], sticks[i]]

    return [-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
