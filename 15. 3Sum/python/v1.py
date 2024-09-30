from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        two_sum = {}
        counter = {}
        unique_nums = set(nums)

        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                two_sum[tuple([nums[i], nums[j]])] = nums[i] + nums[j]

        triplets_seen = set()

        for key, value in two_sum.items():
            key_list = list(key)
            temp_counter = counter.copy()

            if -value in unique_nums:
                triplet = sorted(key_list + [-value])

                valid = True
                for num in triplet:
                    if num in temp_counter and temp_counter[num] > 0:
                        temp_counter[num] -= 1
                    else:
                        valid = False
                        break

                if valid and tuple(triplet) not in triplets_seen:
                    res.append(triplet)
                    triplets_seen.add(tuple(triplet))

        return res
