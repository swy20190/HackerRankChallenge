import os


def pageCount(n, p):
    # Write your code here
    front_flip = int(p/2)
    end_flip = int(n/2)-front_flip
    return min(front_flip, end_flip)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
