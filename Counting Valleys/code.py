import os


def countingValleys(steps, path):
    # Write your code here
    answer = 0
    height = 0

    for i in range(steps):
        if path[i] == 'D':
            height -= 1
        else:
            if height == -1:
                answer += 1
            height += 1
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
