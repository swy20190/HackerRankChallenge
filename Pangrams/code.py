import os


def pangrams(s):
    # Write your code here
    buckets = []
    for i in range(26):
        buckets.append(0)
    for i in range(len(s)):
        char = s[i]
        if char >= 'a' and char <= 'z':
            buckets[ord(char) - ord('a')] += 1
        elif char >= 'A' and char <= 'Z':
            buckets[ord(char[0]) - ord('A')] += 1

    for i in range(26):
        if buckets[i] == 0:
            return "not pangram"
    return "pangram"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
