while True:
    try:
        input_string = input().rstrip()
    except EOFError:
        break
    if input_string:
        answer = ""
        input_list = input_string.split(';')
        if input_list[0] == "S":
            raw = ""
            up_index = []
            if input_list[1] == "M":
                raw = input_list[2][0:-2]
                up_index = [0]
            else:
                if input_list[1] == "V":
                    up_index = [0]
                raw = input_list[2]

            for i in range(len(raw)):
                if raw[i] >= 'A' and raw[i] <= 'Z':
                    up_index.append(i)
            for i in range(len(up_index) - 1):
                word = raw[up_index[i]:up_index[i + 1]]
                word = word[0].lower() + word[1:]
                answer += word
                answer += " "
            end = raw[up_index[-1]:]
            end = end[0].lower() + end[1:]
            answer += end
            print(answer)
        else:
            raw_list = input_list[2].split()
            for word in raw_list:
                answer += word.capitalize()
            if input_list[1] == "M":
                answer = answer[0].lower() + answer[1:]
                answer += "()"
            elif input_list[1] == "V":
                answer = answer[0].lower() + answer[1:]
            print(answer)
    else:
        break

