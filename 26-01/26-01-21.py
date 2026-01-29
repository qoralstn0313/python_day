# N, M = map(int, input().split())
# barkets = [0] * N

# for k in range(N):
#     barkets[k] = k + 1

# for _ in range(M):
#     i, j = map(int, input().split())
#     barkets[i - 1 : j] = barkets[i - 1 : j][::-1]

# print(" ".join(map(str, barkets)))

# N = int(input())
# # nums = []

# # for _ in range(N):
# # nums.append(int(input()))
# # 입력값을 한개씩 받고싶으면 이렇게.
# nums = list(map(int, input().split()))
# # 입력값을 여러개 한번에 받고싶으면 list로 받으면 됨.
# total = 0

# max_num = max(nums)
# for i in range(len(nums)):
#     nums[i] = (nums[i] / max_num) * 100
#     total += nums[i]

# print(total / len(nums))

# # 더 좋은 코드
# n = int(input())
# scores = list(map(int, input().split()))

# m = max(scores)
# new_avg = sum(score / m * 100 for score in scores) / n
# # 기가 막히노
# print(new_avg)

# # sum() 안쓴 버전
# n = int(input())
# scores = list(map(int, input().split()))

# m = max(scores)

# total = 0
# for s in scores:
#     total += s / m * 100

# print(total / n)

words = input()
num = int(input())

print(words[num - 1])
