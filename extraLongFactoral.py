def extraLongFactorals(n):
    total = n
    while n > 1:
        total *= n-1
        n -= 1
    print(total)
    return total

if __name__ == "__main__":
    extraLongFactorals(25)