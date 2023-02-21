        for n in range(1, 1000):
            r = bin(n)[2:]
            if r.count("1") % 2 == 0:
                r=str(r) + "01"
            else:
                r= "1" + str(r) + "10"
            if  int(r, 2)<105:
                print (n)
