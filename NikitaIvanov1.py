from module2 import *
palk=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]
def palgad(p,i):
    valik=input("Средняя зарплата - 1,\n минимальная зарплата - 2,\n максимальная зарплата - 3,\n ищу по имени - 4,\n сортирую - 5, \n добавляю человека - 6\)
    if valik=="1":
        kesk_palk=round(keskmine(palk),2)
        print(" Средняя зарплата ",kesk_palk)
        print()
        print()
    elif valik=="2":
        m_palgad,nimi=minimum(palk,inimesed)
        for n in nimi:
            print(m_palgad[0], " получит человек ",n)
            print()
            print()
    elif valik=="3":max_palk,kto=maksimum(palk,inimesed)
        print("Максимальная зарплата ", max_palk, " будет получено ",kto)
        print()
        print()
    elif valik=="4":                                       
        p,i=delete(palk,inimesed)
        print(palk,inimesed)
        if len(inimesed)==0:
            print("Пустой лист")
        else:
            for i in range(len(inimesed)):
                print(inimesed[i]," будет получено ", palk[i])
    elif valik=="5":
        p,i=sorteerimine(palk,inimesed)
        for i in range(len(inimesed)):
            print(inimesed[i]," будет получено ", palk[i])
            print()
            print()
