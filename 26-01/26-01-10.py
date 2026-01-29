# N = int(input().strip())

# nums = list(map(int, input().split()))

# print(min(nums), max(nums))

# nums = []
# for i in range(9):
#     nums.append(int(input().strip()))

# max_num = max(nums)

# for j in range(9):
#     if nums[j] == max_num:
#         print(max_num)
#         print(j + 1)
#         break


# nums = [int(input()) for i in range(9)]

# max_num = max(nums)
# print(max_num)
# print(nums.index(max_num) + 1)

# list = [1, 2, 3, 4, 5]

# print(list.index(3))

# N, M = map(int, input().split())
# baskets = [0] * N

# for _ in range(M):
#     i, j, k = map(int, input().split())
#     for x in range(i - 1, j):
#         baskets[x] = k

# print(" ".join(map(str, baskets)))

m = [1, 2, 3]
print(" ".join(map(str, m)))
print(m)
