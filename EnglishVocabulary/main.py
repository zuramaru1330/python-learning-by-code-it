# Windows 환경에서는 encoding를 명시를 하지 않으면 File read error 또는
# Type error가 발생하게 된다.
file_pointer = open("vocabulary.txt", "r", encoding = "utf-8")

for voca_read in file_pointer:
    data = voca_read.strip().split(": ")
    english_word = data[0]
    korean_word = data[1]

    answer_input = input("%s: " % (korean_word))

    if answer_input == english_word:
        print("맞았습니다.")
    elif answer_input == 'q':
        break
    else:
        print("아쉽숩니다. 정답은 %s입니다." % (english_word))


file_pointer.close()
