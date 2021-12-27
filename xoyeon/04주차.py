# 2557	 Hello World
print("Hello World!")

# 1000	 A+B
a, b =input().split()
print(int(a)+int(b))

# 10998	 A×B
a, b = map(int, input().split())
print(a*b)

# 1001	 A-B
a, b = input().split()
print(int(a)-int(b))

# 1008	 A/B
a, b = map(float, input().split())
print(round(a/b, 9))

# 10869	 사칙연산
a, b = map(int, input().split())

print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
print(a%b)

# 10430	 나머지
A, B, C = map(int, input().split())
print(int((A+B)%C))
print(int(((A%C) + (B%C))%C))
print(int((A*B)%C))
print(int(((A%C) * (B%C))%C))

# 2558	 A+B - 2
a = int(input())
b = int(input())
print(a+b)

# 2588	 곱셈
i = int(input())
j = input()

print(i * int(j[2]))
print(i * int(j[1]))
print(i * int(j[0]))
print(i * int(j))

# 3046	 R2
r1, s = map(int, input().split())
r2 = 2*s - r1

print(r2)
