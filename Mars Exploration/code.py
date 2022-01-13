import os


def marsExploration(s):
    # Write your code here
    answer = 0
    for i in range(len(s)):
        if i % 3 == 1:
            if s[i] != 'O':
                answer += 1
        else:
            if s[i] != 'S':
                answer += 1

    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
