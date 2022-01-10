import os


def timeConversion(s):
    # Write your code here
    time_str = s[0:8]
    am_pm = s[8:10]
    if am_pm == "AM":
        if time_str[0:2] == "12":
            return "00"+time_str[2:]
        else:
            return time_str
    else:
        if time_str[0:2] == "12":
            return time_str
        else:
            return str(int(time_str[0:2])+12)+time_str[2:]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()