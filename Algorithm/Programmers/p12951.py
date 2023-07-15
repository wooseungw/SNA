def solution(s):
    s = s.lower()
    str = s.split(" ")

    for i, text in enumerate(str) :
        if len(text) != 0 and text[0].isalpha():
            text = text[0].upper() + text[1:]
            str[i] = text

    answer = " ".join(str)
    return answer

print(solution("i 2am    developer          ")+"|")