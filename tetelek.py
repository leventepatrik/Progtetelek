import math
def osztok(szam):
    lista=[]
    for oszto in range(2,(math.sqrt(szam),1)):
        if szam % oszto ==0:
            lista.append(oszto)
        return lista
print(osztok(36))        
            



