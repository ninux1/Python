#!/usr/bin/env python


def mergesort(nums):
        if len(nums) == 1:
            return

        middle_index = len(nums) // 2

        left_half = nums[:middle_index]
        right_half = nums[middle_index+1:]

        mergesort(left_half)
        mergesort(right_half)

        i = j = 0

        while True:
            if i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    nums.append(left_half[i])
                    i += 1
                else:
                    nums.append(right_half[j])
                    j += 1
            elif i == len(left_half) and j < len(right_half):
                nums.append(right_half[j])
                j += 1
            elif j == len(right_half) and i < len(left_half):
                nums.append(left_half[i])
                i += 1
            else:
                if i == len(left_half) and j == len(right_half):
                    break


if __name__ == '__main__':
    nums = [85, 23, 47, 20, 1, 5, 73]
    mergesort(nums)
    print(nums)