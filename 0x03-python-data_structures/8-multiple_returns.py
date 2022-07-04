#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return len(sentence), None
    if sentence is not None:
        length = len(sentence)
        return length, sentence[0]
