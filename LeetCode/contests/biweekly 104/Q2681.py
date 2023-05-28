from typing import List


# TODO
class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        m = len(nums)

        def power_set(s):
            if len(s) == 0:
                return [([], 0, 0)]

            elem = s.pop()

            # Recursively get the power set of the remaining set
            power_set_without_elem = power_set(s)

            # Include the chosen element in all subsets of the power set obtained above
            power_set_with_elem = []
            for subset in power_set_without_elem:
                if not subset[0]:
                    power_set_with_elem.append(
                        (subset[0] + [elem], elem, elem))
                else:
                    power_set_with_elem.append(
                    (subset[0] + [elem], min(subset[1], elem), max(subset[2], elem)))

            # The full power set is the combination of the power set without the chosen element
            # and the power set with the chosen element
            return power_set_without_elem + power_set_with_elem
        p = 0
        for s in power_set(nums):
            p += s[1] * s[2] ** 2
        return p


s = Solution()
print(s.sumOfPower([2,1,4]))