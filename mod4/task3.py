def evk(a, b):
    if b == 0:
        return a
    return evk(b, a % b)
a, b = map(int, input().split())
print(evk(a, b))