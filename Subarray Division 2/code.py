import os


def birthday(s, d, m):
    # Write your code here
    answer = 0
    curr_sum = 0
    for i in range(m):
        curr_sum += s[i]
    if curr_sum == d:
        answer = 1
    for i in range(len(s) - m):
        curr_sum -= s[i]
        curr_sum += s[i + m]
        if curr_sum == d:
            answer += 1
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
