#coding: utf-8

"""
    实现一个栈的逆序，但是只能用递归函数和这个栈本身的pop操作来实现，而不能自己申请另外的数据结构。
    给定一个整数数组A即为给定的栈，同时给定它的大小n，请返回逆序后的栈。

    测试样例：
    [4,3,2,1],4
    返回：[1,2,3,4]
"""

class StackReverse(object):

    def get_and_remove_bottom(self, A):
        result = A.pop()
        if A == []:
            return result

        bottom = self.get_and_remove_bottom(A)
        A.append(result)
        return bottom

    def reverse_(self, A):
        if A == []:
            return

        bottom = self.get_and_remove_bottom(A)
        self.reverse_(A)
        A.append(bottom)
        return A


s = StackReverse()
print s.reverse_([4, 3, 2, 1])