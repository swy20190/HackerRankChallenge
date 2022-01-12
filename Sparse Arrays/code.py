import os


def matchingStrings(strings, queries):
    # Write your code here
    result_dict = {}
    answer = []
    for que in queries:
        if que in result_dict:
            answer.append(result_dict[que])
        else:
            times = 0
            for sentence in strings:
                if sentence==que:
                    times += 1
            answer.append(times)
            result_dict[que] = times
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
