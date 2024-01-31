def feladat2():
    a=42
    f=67
    i=a
    while (i <=f and not(i%10==0)):
        i+=1
        van:bool = i == f
        if(van):
            print(f"van 0-ra végződő szám:"+i)
        else:
            print(f"nincs 0-ra végződő szám:")
