# c i=0 выводятся числа со второго элемента из списка
s = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i < len(s):
    i += 1
    if s[i] > 0:
        print(s[i])
        continue
    if s[i] < 0:
        break
# c i=1 выводятся числа с первого элемента из списка
s = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = -1
while i < len(s):
    i += 1
    if s[i] > 0:
        print(s[i])
        continue
    if s[i] < 0:
        break
