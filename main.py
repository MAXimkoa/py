a = "KLMNO"
n = 0
for b in a:
     for c in a:
         for d in a:
             for e in a:
                 for f in a:
                     w = b + c + d + e + f
                     if (w[0]== "L" or w[1]== "L" or w[2]== "L" or w[3]== "L") and w[4]=="M":
                         if w[0] != w[2] and w[2] != w[4]:
                             if w[1] != w[3]:
                                 n+=1
print(n)