# Exercise 1

# 1. O(1)
# 2. O(n^2)
# 3. O(log n)


def insertion_sort(numbers: list) -> None:
    for i in range(1, len(numbers)):
        cursor = numbers[i]
        j = i - 1         
        while j >= 0 and cursor< numbers[j]:
            numbers[j+1] = numbers[j]
            j -=1
        numbers[j+1] = cursor


def binary_search(numbers: list, value: int) -> int:
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2 #This performs integer division
        if numbers[mid] == value:
            return mid
        elif value > numbers[mid]:
            left = mid + 1
        else:
            right = mid-1
    return -1


# numbers = [5, 2, 9, 1, 5, 6]
# insertion_sort(numbers) # sorts the numbers list
# print(numbers) # check that the sorting is successfull

numbers = [1, 3, 5, 7, 9, 11]
print(binary_search(numbers, 7))