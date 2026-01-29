# print("크리스마스 이브")
# print("크리스마스 * 3")
# print("크리스마스" + "3")
# print("크리스마스" * "3") > 오류
# print("크리스마스" * 3)

# print("크리스마스"[4])
# print("크리스마스"[-1])
# print("크리스마스"[1:4]) 시작값~(마지막값-1)
# print(len("크리스마스")) len > 문자열 수

# print("\\\\\\\\") > \\ = \를 뜻함
# print("크리스마스"[1])
# print("크리스마스"[2])

# A = int(input("A의 값을 입력해주시오.(A > 0): "))
# B = int(input("B의 값을 입력해주시오.(B < 10): "))
# print(A + B)

# print(type(512))
# print(type(3.12))

# print("3 + 4 =", 3 + 4)
# print(3462 // 17)
# print(3462 % 17)
# print("- 몫: 3462 // 17")
# print("- 몫:", 3462 // 17)

# print(2 - 2 + 2 / 2 * 2 + 2)
# print(2 + 2 - 2 * 2 / 2 * 2)
# pi = 3.141592
# print(pi)
# print("pi")

# string = input("인사해봐: ")
# print(string)


# 집 평수 계산 해주는 프로그램

# 가로 m^2과 세로 m^2 수치를 입력받습니다.
input1 = input("m^2 단위의 가로 길이를 알려주세요: ")
input2 = input("m^2 단위의 세로 길이를 알려주세요: ")

# 받은 데이터를 숫자 자료형으로 변경하고 공식을 통해 집 평수를 계산합니다
width = float(input1)
length = float(input2)

size = (width * length) / 3.3

# 출력합니다.
print("가로", width, "m^2와", "세로", length, "m^2의 집 평수는", size, "입니다.")

# .format() 사용한다면
print("가로 {}m^2와 세로 {}m^의 평수는 {}입니다.".format(width, length, size))
