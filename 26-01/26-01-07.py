# for i in reversed(range(5)):
#     print(i)

# for i in range(5, 0, -1):
#     print(i)

# star = int(input().strip())

# for i in range(1, star + 1, 1):
#     print("*" * i)


# star = int(input().strip())
# output = ""

# for i in range(1, star + 1):
#     for j in range(star, i, -1):
#         output += " "
#     for k in range(0, (2 * i - 1)):
#         output += "*"
#     output += "\n"

# print(output)

# N = int(input().strip())
# output = ""

# for i in range(1, N + 1):
#     for j in range(N, i, -1):
#         output += " "
#     for k in range(i):
#         output += "*"
#     output += "\n"
# print(output)

# N = int(input().strip())

# for i in range(1, N + 1):
#     for j in range(N, i, -1):
#         print(" ", end="")
#     for k in range(i):
#         print("*", end="")
#     print("")


# A, B = map(int, input().split())
# print(f"{A+B}")

# i = 0
# while True:
#     print(f"{i}번째 반복문입니다.")
#     i += 1
#     text = input("종료하시겠습니까? (y/n): ")
#     if text in ["y", "Y"]:
#         print("종료합니다.")
#         break

# for i in range(0, 10, 3):
#     print(i)

while True:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except:
        break
