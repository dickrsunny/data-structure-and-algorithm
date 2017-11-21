#coding: utf-8

class SStack(object):

    def __init__(self):
        self.elems = []

    def push(self, elem):
        self.elems.append(elem)

    def pop(self):
        elem = self.elems[-1]
        self.elems.pop()
        return elem

def check_parens(str_):
    parens = '()[]{}'
    left_parens = '([{'
    opposite_parens = {')': '(', ']': '[', '}': '{'}

    def parenfinder(str_):
        i, length = 0, len(str_)
        while i < length:
            while str_[i] not in parens:
                i += 1
            if i == length:
                return
            yield str_[i], i
            i += 1

    s = SStack()

    for item, j in parenfinder(str_):
        if item in left_parens:
            s.push(item)
        else:
            res = s.pop()
            if res != opposite_parens[item]:
                return False
    return True

print check_parens('(q[w{e}])')