def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*4, reverse=False)
    return str(int(''.join(numbers)))


print(solution([30, 34, 3, 9, 5]))

# arr = ["3", "9", "30", "5", "34", "31", "32"]
# print(arr)
# arr.sort()
# print(arr)

# a = ["a", "abc", "cedf", "1234", "d"]

# result = sorted(arr, key=lambda x: x*3)

# print(result)
