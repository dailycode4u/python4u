#Calculating Pi using the Leibniz formula
def picalc(num: int) -> float:
    pi: float = 0
    numerator: float = 4
    denominator: float = 1
    operation: float = 1
    for _ in range(num):
        pi += operation * (numerator / denominator)
        denominator += 2
        operation *= -1
    return print(pi)
picalc(10000)