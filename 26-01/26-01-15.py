# N, M = map(int, input().split())
# baskets = [0] * N

# for k in range(N):
#     baskets[k] = k + 1
# # baskets = [0] * N
# # for k in range(N):
# #     baskets[k] = k + 1
# change = [0]
# for _ in range(M):
#     i, j = map(int, input().split())
#     change[0] = baskets[i - 1]
#     baskets[i - 1] = baskets[j - 1]
#     baskets[j - 1] = change[0]
# # baskets[i-1], baskets[j-1] = baskets[j-1], baskets[i-1]

# print(" ".join(map(str, baskets)))
# N = []

# for _ in range(28):
#     N.append(int(input().strip()))
# # N = set(int(input()) for _ in range(28))

# for i in range(1, 31):
#     if i not in N:
#         print(i)


# for i in range(10):
#     for j in range(10, 1, -1):
#         print(" ", end="")
#     for k in range(11):
#         print("*", end="")

# output = ""

# for i in range(1, 15):
#     for j in range(14, i, -1):
#         output += " "
#     for k in range(0, 2 * i - 1):
#         output += "*"
#     output += "\n"
# print(output)


# def print_3times(a):
#     print(a)
#     print(a)
#     print(a)
# print_3times("안녕하세요")
# print_3times(13)


# def print_n_times(value, n):
#     for _ in range(n):
#         print(value)


# print_n_times("안녕하세요", 4)


def print_n_times(n, **values):
    for i in range(n):
        for key, value in values.items():
            print(key, value)
        print()


print_n_times(2, name="alstn", age=23)
