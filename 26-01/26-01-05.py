# list = [[1, 2, 3], [4, 5, 6, 7], [8, 9]]

# # for nums in list:
# #     for num in list:
# #         print(nums)
# b = [*list, ["apple"]]
# b.append(100)

# print(b)

# num = [100, 30, 3, 399, 99, 9]

# for i in num:
#     if i // 10 >= 10:
#         print("3자리")
#     elif i // 10 >= 1:
#         print("2자리")
#     else:
#         print("1자리")

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# output = [[], [], []]

# for number in numbers:
#     output[(number + 2) % 3].append(number)

# print(output)

# N = int(input().strip())

# for i in range(1, 10):
#     print(f"{N} * {i} = {N * i}")


# T = int(input().strip())

# for i in range(0, T):
#     A, B = map(int, input().split())
#     print(A + B)

# N = int(input().strip())
# k = 0

# for i in range(1, N + 1):
#     k += i
# print(k)

# dictionary = {"name": "백민수", "age": "23"}

# key = input().strip()

# if key in dictionary:
#     print(dictionary[key])
# else:
#     print("그런값은 없다")


# numbers = [1, 4, 2, 6, 4, 1, 2, 6, 3, 6, 2, 5, 3, 4, 9, 1]
# counter = {}

# for number in numbers:
#     if number in counter:
#         counter[number] += 1
#     else:
#         counter[number] = 1
# print(counter)

# total = int(input().strip())
# num = int(input().strip())
# totals = 0
# for i in range(num):
#     A, B = map(int, input().split())
#     totals += A * B
# if totals == total:
#     print("Yes")
# else:
#     print("No")

# N = int(input().strip())
# print(("long " * (N // 4)).strip() + " int")


N = int(input())

for i in range(N // 4):
    print("long", end=" ")

print("int")
