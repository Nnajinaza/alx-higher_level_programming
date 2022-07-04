#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return len(sentence), None
    if sentence is not None:
        length = len(sentence)
        if sentence[0] >= 'A' and sentence[0] <= 'Z':
            return length, sentence[0]
        elif sentence[0] >= 'a' and sentence[0] <= 'z':
            return length, sentence[0]
