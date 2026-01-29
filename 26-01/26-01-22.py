# word = input()

# print(len(word))

# N = int(input())

# for _ in range(N):
#     word = input()
#     length = int(len(word))
#     print(f"{word[0]}{word[length-1]}")

# N = int(input())

# for _ in range(N):
#     word = input()
#     print(word[0] + word[-1])

# print(ord(input()))

# N = int(input())

# nums = input()

# print(sum(int(x) for x in nums))

S = input()

for i in range(26):
    alphabet = chr(ord("a") + i)
    print(S.find(alphabet), end=" ")
