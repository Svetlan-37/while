s = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i < len(s):
    if s[i] > 0:
        print(s[i])
    i += 1
    if s[i] < 0:
        break
