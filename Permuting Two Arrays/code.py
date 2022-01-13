import os


def twoArrays(k, A, B):
    # Write your code here
    A.sort()
    B.sort()
    n = len(A)
    for i in range(n):
        paired = False
        for j in range(n):
            if B[j] >= 0:
                if A[n - 1 - i] + B[j] >= k:
                    B[j] = -1
                    paired = True
                    break
        if not paired:
            return "NO"
    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()