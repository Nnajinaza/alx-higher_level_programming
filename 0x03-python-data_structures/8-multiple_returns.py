#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return len(sentence), None
    elif sentence is not None:
        return len(sentence), sentence[0]
