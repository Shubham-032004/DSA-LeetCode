# class Solution(object):
#     def threeSum(self, nums):
#         n = len(nums)
#         my_set = set()

#         for i in range(n):
#             for j in range(i + 1, n):
#                 for k in range(j + 1, n):

#                     if nums[i] + nums[j] + nums[k] == 0:
#                         temp = [nums[i], nums[j], nums[k]]
#                         temp.sort()
#                         my_set.add(tuple(temp))

#         return [list(ans) for ans in my_set]


# class Solution(object):
#     def threeSum(self, nums):
#         nums.sort()
#         ans = []
#         n = len(nums)

#         for i in range(n - 2):

#             # Skip duplicate first element
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue

#             left = i + 1
#             right = n - 1

#             while left < right:

#                 total = nums[i] + nums[left] + nums[right]

#                 if total == 0:
#                     ans.append([nums[i], nums[left], nums[right]])

#                     left += 1
#                     right -= 1

#                     # Skip duplicate left values
#                     while left < right and nums[left] == nums[left - 1]:
#                         left += 1

#                     # Skip duplicate right values
#                     while left < right and nums[right] == nums[right + 1]:
#                         right -= 1

#                 elif total < 0:
#                     left += 1

#                 else:
#                     right -= 1

#         return ans



class Solution(object):
    def threeSum(self, nums):
        n = len(nums)
        result = set()

        for i in range(n):
            my_set = set()

            for j in range(i + 1, n):
                third = -(nums[i] + nums[j])

                if third in my_set:
                    temp = [nums[i], nums[j], third]
                    temp.sort()
                    result.add(tuple(temp))

                my_set.add(nums[j])

        return [list(ans) for ans in result]