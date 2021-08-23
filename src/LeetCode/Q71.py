# 71. Simplify Path
# Given a string path, which is an absolute path (starting with a slash '/')
# to a file or directory in a Unix-style file system, convert it to the simplified canonical path.
# In a Unix-style file system, a period '.' refers to the current directory,
# a double period '..' refers to the directory up a level,
# and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'.
# For this problem, any other format of periods such as '...' are treated as file/directory names.

# The canonical path should have the following format:
# The path starts with a single slash '/'.
# Any two directories are separated by a single slash '/'.
# The path does not end with a trailing '/'.
# The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
# Return the simplified canonical path.
# Scott 2021/08/23

class Solution:

    # Same idea as mine
    # 86.89%
    def simplifyPath2(self, path: str) -> str:
        stack = []
        n = len(path)
        for item in path.split('/'):
            if item == '.' or item == '':
                continue
            elif item == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(item)
        return '/' + '/'.join(stack)

    # Original
    # 95.17%
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0
        n = len(path)
        while i < n - 1:
            c = path[i]
            if c == '/':
                i += 1
                while i < n and path[i] == '/':
                    i += 1
                start = i
                while i < n:
                    if path[i] == '/':
                        break
                    i += 1
                s = path[start:i]
                if s == '.':
                    pass
                elif s == '..':
                    if stack:
                        stack.pop()
                elif '/' in s:
                    pass
                elif not s:
                    pass
                else:
                    stack.append(s)
        return '/' + '/'.join(stack)


if __name__ == '__main__':
    print(Solution().simplifyPath("/home/"))
    print(Solution().simplifyPath("/../"))
    print(Solution().simplifyPath("/home//foo/"))
    print(Solution().simplifyPath("/a/./b/../../c/"))
    print(Solution().simplifyPath("/a/../../b/../c//.//"))
    print(Solution().simplifyPath("/a//b////c/d//././/.."))
    print(Solution().simplifyPath("/a/../../b/../c//.//"))

    print("===================================================================")

    print(Solution().simplifyPath2("/home/"))
    print(Solution().simplifyPath2("/../"))
    print(Solution().simplifyPath2("/home//foo/"))
    print(Solution().simplifyPath2("/a/./b/../../c/"))
    print(Solution().simplifyPath2("/a/../../b/../c//.//"))
    print(Solution().simplifyPath2("/a//b////c/d//././/.."))
    print(Solution().simplifyPath2("/a/../../b/../c//.//"))
