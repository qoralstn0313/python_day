# A = int(input().strip())
# B = int(input().strip())
# ones = B % 10
# tens = (B // 10) % 10
# hund = B // 100
# print(A * ones)
# print(A * tens)
# print(A * hund)
# print(A * B)

# # 문자화 시키고 계산도 가능
# b = str(B)

# print(A * int(b[2]))
# print(A * int(b[1]))
# print(A * int(b[0]))
# print(A * B)

# A, B, C = map(int, input().split())
# print(f"{A + B + C}")

# 문자열에선 \ 출력하려면 \\쓰기
# print("\\   /\\")
# print(" ) ( ')")
# print("(  /  )")
# print(" \\(__)|")

# print(10 == 100)
# print("안녕" in "안녕")

# if True:
#     print("참이용")

# num = int(input("숫자를 입력하세요: ").strip())

# if num > 100:
#     print("100 이상입니다")
# elif num == 100:
#     print("100 입니다.")
# else:
#     print("100 이하입니다.")


# import datetime

# now = datetime.datetime.now()

# # if now.hour < 12:
# #     print(f"현재 시각은{now.hour}시로 오전입니다.")

# # if now.hour >= 12:
# #     print(f"현재 시각은 {now.hour}시로 오후입니다!")

# if now.hour < 12:
#     print(f"현재 시각은 {now.hour}시로 오전입니다.")
# else:
#     print(f"현재 시각은 {now.hour}시로 오후입니다.")

# x = 10
# y = 2

# if x > 4:
#     if y > 1:
#         print(x * y)
# else:
#     print(x + y)

# A, B = map(int, input().split())

# if A > B:
#     print(">")
# elif A == B:
#     print("==")
# else:
#     print("<")


# nums = int(input().strip())

# if 90 <= nums <= 100:
#     print("A")
# elif 80 <= nums < 90:
#     print("B")
# elif 70 <= nums < 80:
#     print("C")
# elif 60 <= nums < 70:
#     print("D")
# else:
#     print("F")

# year = int(input().strip())

# if year % 4 == 0:
#     if year % 100 != 0 or year % 400 == 0:
#         print("1")
#     else:
#         print("0")
# else:
#     print("0")
