"""Given an array of integers and a target,
return indices of two numbers that add up to the target."""


def two_sum(nums, target):
    """Given an array of integers and a target,
    return indices of two numbers that add up to the target."""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def _two_sum2(nums, target):
    """Given an array of integers and a target,
    return indices of two numbers that add up to the target."""
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))
    print(_two_sum2(nums, target))
