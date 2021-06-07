def fact1(n):
    if n <= 1:
        return 1 # 탈출하는 것을 만들어 주는 것
    return n * fact1(n-1)

print(fact1(5))