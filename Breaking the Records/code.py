import os

def breakingRecords(scores):
    # Write your code here
    max_score = -1
    min_score = -1
    max_break = 0
    min_break = 0
    for s in scores:
        if max_score == -1:
            max_score = s
        if min_score == -1:
            min_score = s
        if s<min_score:
            min_break += 1
            min_score = s
        if s>max_score:
            max_break += 1
            max_score = s
    return [max_break, min_break]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
