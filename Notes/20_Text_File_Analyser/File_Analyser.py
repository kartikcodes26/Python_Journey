'''
Example text used:

Hello My name is kartik
i am 18 years old
i am a boy
i live in kalyan
'''

import re


def analyse(filename):
    with open(filename, 'r') as f:
        chars = 0
        words = 0
        lines = 0
        sentences = 0
        for line in f:
            sentences += len(re.findall(r"[.!?]+(?=\s|$)", line))# Vibecoded
            lines += 1
            chars += len(line)
            words += len(line.split())

        return (chars, words, lines, sentences)


print(analyse('Example.txt'))
