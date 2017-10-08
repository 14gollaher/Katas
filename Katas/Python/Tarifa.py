# https://open.kattis.com/problems/tarifa

def main():
    monthlyDataAllowed = int(input())
    numberMonthsUsed = int(input())

    dataAllowed = monthlyDataAllowed
    for monthUsage in getMonthlyUsage(numberMonthsUsed):
        dataAllowed += (monthlyDataAllowed - monthUsage)
    print(dataAllowed)

def getMonthlyUsage(numberMonthsUsed):
    for i in range(numberMonthsUsed):
        yield int(input())

main()


