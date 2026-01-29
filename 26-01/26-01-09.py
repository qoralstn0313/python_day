# codon = input("코돈을 입력하시오: ").strip()

# counter = {}

# for i in range(0, len(codon), 3):
#     list = codon[i : i + 3]
#     if len(list) == 3:
#         if list not in counter:
#             counter[list] = 0
#         counter[list] += 1

# print(counter)

# a = [1, 2, [3, 4], 5, [6, 7, 8]]
# new_list = []

# for i in a:
#     if type(i) == list:
#         for j in i:
#             new_list.append(j)
#     else:
#         new_list.append(i)

# print(new_list)
# list = []
# aa = [1, 2]
# list.append(3)
# list.append([1, 2])
# list.append(int(aa))

# print(list)


# a = [1, 2]
# print(type(a))
# list = 1
# print(type(list))


# N, X = map(int, input().split())
# A = list(map(int, input().split()))
# B = []

# for i in A:
#     if i < X:
#         B.append(i)

# print(" ".join(map(str, B)))


def plus():
    print("하이")


plus()
