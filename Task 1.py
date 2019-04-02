first = list(map(int, input("Введите первый список: ").split()))
second = list(map(int, input("Введите второй список: ").split()))
n = len(first)
i = int(0)
iter = int(0)
while(iter < n):
    print("Рассматриваемый элемент ", first[i])
    if (second.count(first[i]) == 0) :
        first.append(first[i])
        first.pop(i)
    else: i = i + 1
    iter = iter + 1
    print(first)