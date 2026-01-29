# list = reversed([1, 2, 3, 4, 5, 6])

# for i in list:
#     print("첫 번째 반복문: {}".format(i))

# for i in list:
#     print("두 번째 반복문: {}".format(i))

# list = ["요소 A", "요소 B", "요소 C"]

# # for i in range(len(list)):
# #     print(f"{i}번째 요소는 {list[i]}입니다.")

# for index, value in enumerate(list):
#     print(f"{index}번째 요소는 {value}입니다.")

# list = {"name": "민수", "age": 23, "major": "software"}

# for k, e in list.items():
#     print(f"list[{k}]: {e}")


# list = [1, 2, 3, 4, 5]

# print(" ".join(map(str, list)))

# N = int(input())
# nums = list(map(int, input().split()))
# v = int(input())

# print(nums.count(v))

# list = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]
# dic_list = {}

# for i in list:
#     if i not in dic_list:
#         dic_list[i] = 0
#     dic_list[i] += 1

# print(f"{list}에서")
# print(f"사용된 숫자의 종류는{len(dic_list)}개 입니다.")
# print(f"참고: {dic_list}")

DNA = input("염기 서열을 입력해주세요: ").strip()

counter = {"a": 0, "t": 0, "g": 0, "c": 0}

for dna in DNA:
    counter[dna] += 1
for key in counter:
    print(f"{key}의 개수: {counter[key]}")
