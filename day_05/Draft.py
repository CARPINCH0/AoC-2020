Q = []
N = 128
N2 = 8
L = [iter * 8 for iter in range(N)]
print (L)


for i in L:
    Q.append(i+1)
    Q.append(i+2)
    Q.append(i+3)
    Q.append(i+4)
    Q.append(i+5)
    Q.append(i+6)
    Q.append(i+7)


def Diff(Q, SitL):
    li_dif = [i for i in Q + SitL if i not in Q or i not in SitL]
    return li_dif
 

eSitL = Diff(Q, SitL)
print(eSitL)