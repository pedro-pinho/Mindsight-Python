
def fibonacci(n):
    vetor = [0, 1]
    for i in range(2, n+1):
        vetor.append(vetor[-1] + vetor[-2])
    return vetor

print(fibonacci(40))