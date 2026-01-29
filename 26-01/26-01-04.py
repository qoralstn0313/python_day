# x = int(input().strip())
# y = int(input().strip())

# if x > 0 and y > 0:
#     quadrant = 1
# elif x < 0 and y > 0:
#     quadrant = 2
# elif x < 0 and y < 0:
#     quadrant = 3
# else:
#     quadrant = 4
# print(quadrant)

# H, M = map(int, input().split())

# if M >= 45:
#     print(f"{H} {M-45}")
# else:
#     H = 23 if H == 0 else H - 1
#     print(f"{H} {M+15}")

# H, M = map(int, input().split())
# T = int(input().strip())

# total = (H * 60 + M + T) % 1440

# print(f"{total // 60} {total % 60}")


# x, y, z = map(int, input().split())

# if x == y == z:
#     print(10000 + x * 1000)
# elif x == y:
#     print(1000 + x * 100)
# elif y == z:
#     print(1000 + y * 100)
# elif z == x:
#     print(1000 + x * 100)
# elif x > y and x > z:
#     print(x * 100)
# elif y > x and y > z:
#     print(y * 100)
# else:
#     print(z * 100)

list = [0, "이디아카페", True, [1, 2, 3]]
# print(list[0])
# print(list[1][2])
# print(list[-1])
# print(list[3][-2])
list.append(3)
list.insert(0, "침입")
del list[-2:]
print(list)
