def lisamine(palk,inimesed):
    top,inimes=sorteerimine(palk,inimesed)
    k= int(input("Выберите значение : " ))
    palk.reverse()
    inimesed.reverse()
    for i in range(0,k,1):
        print(palk[i])
        print(inimesed[i])
    return palk, inimesed
    print()
    print()

def otsing(palk,inimesed):
    add=input("Имя человека:  ")
    inimesed.append(add)
    add_palk=int(input("Зарплата человека:  " ))
    palk.append(add_palk)
    return i,p
    print()
    print()

    def otsing_nimi_jargi(inimesed:list,palgad:list):
        """
        :rtype var: tulemus
        """
        nimi=input("Keda otsime?")
        for inimene in inimesed:
            if inimene.upper()==nimi.upper():
                n=inimesed.count(nimi)
                print("Inimene on olemas,selline nimi kohtume",n,"korda")
                b=-1
                for i in range(n):
                    k=inimesed.index(nimi)
                    palk=palgad[k]
                    print(nimi,palk)
                    

            else:
                t="Ei ole nimekirjas"
                return t

