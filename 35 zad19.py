list=[9,9,9,9,1,1,15,4,22,2,20,20]
q=sorted(list)
print('Lista posortowana rosnąco', q) #tutaj sortuje liste rosnoca
w=input('Podana liczba przez uzytkownika, ktora trzeba sprawdzic na liscie')
l=len(q)

a = 0
w=int(w)
right= l - 1

right=int(right)
z=0
while a < right:
    middle = (a + right)/ 2
    middle = int(middle)
    print('liczba srodkowa', middle)
    if q[middle] < w:
        a=middle+1

        print('LICZBA LEWA',a)
    else:
        right=middle

        print('LICZBA PRAWA', right)
    print('----------------------------')
    z=z+1
    #l = q[middle]
    print('to jest liczba interacji',z)
    print('---')
if q[right] == w:
    print('ZNALEZIONO LICZBE')
    print('Ale trzeba sprawdzić czy poprzednia lub następna w szeregu też jest',w)
    right=int(right)
    print('pozucja liczby poczatkowa',right)
    length1 = l - 1
    print(length1)

    zl=length1*(-1)
    print(zl)

    c=1
    kk=[right]
    for c in range(1,length1):

        o=right+c
        o=int(o)
        print('pozycja przesunieta w prawo o jedna',o)
        oo=right-c

        print('pozycja przesunieta w lewo o jedna',oo)
        if q[o]==w:
            pp=q[o]
            print('liczba wystepuje rowniez dla pozycji',o,'i jes to liczba', pp)

        elif q[oo]==w:
            ppp = q[oo]
            print('liczba wystepuje rowniez dla pozycji', ppp)
        else:

            print('nie wystepuje żaden dubel')
            break
        c=c+1
        kk.append(o)
        print(kk)

    p=q[right]
    print(p,'znajduje sie w liscie na miejscach',kk)
    t=right
    print('to jest ta liczba', p,'znajduje sie na mniejscu',t)
    print('liczba srodkowa', middle)
    #print('liczba srodkowa', middle,'znaleziona liczba',l)
else:
    print('Nie wyjasniony blad')