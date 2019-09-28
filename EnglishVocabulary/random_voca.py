from random import randint
FILE_POINTER = open("vocabulary.txt", "r", encoding = "utf-8")
voca = {}

def voca_read_func():
    for voca_read_loop in FILE_POINTER:
       DATA = voca_read_loop.strip().split(": ")
       voca[DATA[1]] = {DATA[0]}

def voca_quiz_time_func():
    for voca_quiz_loop in range(0,len(voca.values()))


FILE_POINTER.close()