# 722. Remove Comments
# Given a C++ program, remove comments from it. The program source is an array of strings source where source[i] is the ith line of the source code.
#  This represents the result of splitting the original source code string by the newline character '\n'.
# In C++, there are two types of comments, line comments, and block comments.
# The string "//" denotes a line comment, which represents that it and the rest of the characters to the right of it in the same line should be ignored.
# The string "/*" denotes a block comment, which represents that all characters until the next (non-overlapping) occurrence of "*/" should be ignored. 
# (Here, occurrences happen in reading order: line by line from left to right.) 
# To be clear, the string "/*/" does not yet end the block comment, as the ending would be overlapping the beginning.
# The first effective comment takes precedence over others.
# For example, if the string "//" occurs in a block comment, it is ignored.
# Similarly, if the string "/*" occurs in a line or block comment, it is also ignored.
# If a certain line of code is empty after removing comments, you must not output that line: each string in the answer list will be non-empty.
# There will be no control characters, single quote, or double quote characters.
# For example, source = "string s = "/* Not a comment. */";" will not be a test case.
# Also, nothing else such as defines or macros will interfere with the comments.
# It is guaranteed that every open block comment will eventually be closed, so "/*" outside of a line or block comment always starts a new comment.
# Finally, implicit newline characters can be deleted by block comments. Please see the examples below for details.
# After removing the comments from the source code, return the source code in the same format.
# Scott 2021/08/17

from typing import List

class Solution:

    # Original
    # 95.60% 
    # Time O(n) n = The total amount of chars in source
    # Space O(n)
    def removeComments1(self, source: List[str]) -> List[str]:
        delete1 = False
        delete2 = False
        new_source = []
        result = ''
        for i in range(len(source)):
            string = source[i]
            j = 0
            n = len(string)
            while j < n:
                c = string[j]
                if c == '/':
                    if j != n - 1:
                        next_c = string[j + 1]
                        if next_c == '/':
                            if not delete2:
                                delete1 = True
                                j += 1
                        elif next_c == '*':
                            if not delete1 and not delete2:
                                delete2 = True
                                j += 1
                elif c == '*':
                    if not delete1:
                        if j != n - 1:
                            next_c = string[j + 1]
                            if next_c == '/':
                                if delete2:
                                    delete2 = False
                                    j += 2
                                    continue
                if not delete1 and not delete2:
                    result += c
                j += 1
            else:
                if delete1:
                    delete1 = False
            if len(result) != 0:
                if not delete2:
                    new_source.append(result)
                    result = ''
        return new_source


if __name__ == '__main__':
    print(Solution().removeComments1(["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"])
            == ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"])
    print(Solution().removeComments1(["a/*comment", "line", "more_comment*/b"])
            == ["ab"])
    print(Solution().removeComments1(["void func(int k) {", "// this function does nothing /*", "   k = k*2/4;", "   k = k/2;*/", "}"])
            == ["void func(int k) {","   k = k*2/4;","   k = k/2;*/","}"])
    print(Solution().removeComments1(["main() {", "/* here is commments", "  // still comments */", "   double s = 33;", "   cout << s;", "}"])
            == ["main() {","   double s = 33;","   cout << s;","}"])
    print(Solution().removeComments1(["a//*b/*/c","blank","d/*/e/*/f"]) == ["a","blank","df"])
        