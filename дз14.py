import random


def sort(nums):
    sorted = nums.copy()
    for i in range(len(sorted)):
        for j in range(i, len(sorted)):
            if sorted[i] > sorted[j]:
                sorted[i], sorted[j] = sorted[j], sorted[i]

    return sorted


numbers = [random.randint(0, 100) for _ in range(15)]
print(numbers)
print(sort(numbers))
