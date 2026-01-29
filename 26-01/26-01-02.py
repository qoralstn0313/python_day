# text = input("하고싶은 말: ").strip()

# print(f"길이: {len(text)}")
# print(f"'하' 포함? {'하' in text}")
# print(text)

# a = int(input("> 첫번째 숫자: "))
# b = int(input("> 두번째 숫자: "))
# print()
# print("{} + {} = {}".format(a, b, a + b))

# string = "hello"
# string.upper()
# print("a 지점:", string)
# print()
# print("b 지점:", string.upper())

# 153p 도전문제
# 구의 부피와 겉넓이 구하기


# r = int(input("구의 반지름을 입력해주세요: ").strip())
# # int > folat로 바꾸기
# pi = float(3.141592)
# # float 빼기
# vo = (4 / 3) * pi * (r * r * r)
# ex = 4 * pi * (r * r)
# # r ** 2 , r ** 3
# print(f"구의 부피는 {vo}입니다.")
# print("구의 겉넓이는 {}입니다.".format(ex))

# 피타고라스의 정리

# base = float(input("밑변의 길이를 입력해주세요: ").strip())
# height = float(input("높이의 길이를 입력해주세요: ").strip())

# length = ((base**2) + (height**2)) ** (1 / 2)
# print(f"빗변의 길이는 {length}입니다.")

# A, B = map(int, input().split())
# print(A - B)

# A, B = map(int, input().split())
# print(A + B)
# print(A - B)
# print(A * B)
# print(A // B)
# print(A % B)

# name = input().strip()
# print(name + "!??")

# year = int(input().strip())
# print(f"{year - 543}")

# A, B, C = map(int, input().split())
# print((A + B) % C)
# print(((A % C) + (B % C)) % C)
# print((A * B) % C)
# print(((A % C) * (B % C)) % C)

A, B = map(int, input().split())
print("{1:2}".format(B))
