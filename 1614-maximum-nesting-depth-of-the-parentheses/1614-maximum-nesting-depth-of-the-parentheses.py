# class Solution(object):
#     def maxDepth(self, s):
#         max_depth = 0
#         curr_depth = 0
#         stack = []
#         for brac in s:
#             if brac == '(':
#              curr_depth+=1
#              max_depth = max(max_depth,curr_depth)
#             elif brac == ')':
#                 curr_depth -= 1
#                 stack.pop()
#         return max_depth


class Solution(object):
    def maxDepth(self, s):
        max_depth = 0
        curr_depth = 0

        for brac in s:
            if brac == '(':
                curr_depth += 1
                max_depth = max(max_depth, curr_depth)

            elif brac == ')':
                curr_depth -= 1

        return max_depth
        