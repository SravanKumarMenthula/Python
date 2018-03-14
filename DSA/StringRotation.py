''' Rotating a string by d characters'''

s ="IDEONE"
T= ''

d = int(input())
i = 0

while(i < len(s)):
	T = T + s[(i+d)%len(s)]
	i = i + 1

print(T)
