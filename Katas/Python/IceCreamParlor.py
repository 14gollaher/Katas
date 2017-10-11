def solve(money, n, iceCreamCosts):

    sortedIceCreamCosts = iceCreamCosts
    sortedIceCreamCosts.sort()

    for item in iceCreamCosts:
        i = int(n / 2)
        x = i
        while True:
            total = item + iceCreamCosts[i]
            if total is money:
                #a = iceCreamCosts index of item
                #b = iceCreamCosts index of iceCreamCosts[i]
                return str(a) + " " + str(b)
            elif total < money:
                if x is 1 or x is n:
                    break
                x = int(x / 2)
                i += x
            elif total > money:
                if x is 1 or x is n:
                    break
                x = int(x / 2)
                i -= x

t = int(input().strip())
for a0 in range(t):
    m = int(input().strip())
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    print(solve(m, n, a))
