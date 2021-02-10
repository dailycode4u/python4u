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
if __name__ == "__main__":
    """The more terms in the infinite series (the higher the value of num when picalc is called),
    the more accurate the ultimate calculation of pi will be."""
    picalc(10000)
