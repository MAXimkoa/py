for n in range(1, 1000):
    r = 2 * n
    r = bin(r)[2:]
    r = str(r) + str(r.count("1") % 2)
    r = str(r) + str(r.count("1") % 2)
    if int(r, 2) > 123:
        print(n)
        break
