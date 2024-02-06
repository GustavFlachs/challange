print("Vítejte v programu který převádí dekadickou IP adressu na binární ip adressu (prosím rozdělte na 4 části,nepoužívejte tečky prosím)")

a = int(input("Zadejte první část dekadické IP adressi: "))
b = int(input("Zadejte druhou část dekadické IP adressi: "))
c = int(input("Zadejte třetí část dekadické IP adressi: "))
d = int(input("Zadejte čtvrtou část dekadické IP adressi: : "))

výsledek_a = str
výsledek_b = str
výsledek_c = str
výsledek_d = str



if a > 255:
    print("nesmí být více jak 255")
else:
    if a > 127:
        print("1")
        výsledek_a = (a-128)
    else:
        print("0")
    if a > 63:
        print("1")
        výsledek_a = (výsledek_a-64)
    else:
        print("0")
    if a > 31:
        print("1")
        a-32
    else:
        print("0")
    if a > 15:
        print("1")
        a-16
    else:
        print("0")
    if a > 7:
        print("1")
        a-8
    else:
        print("0")
    if a > 3:
        print("1")
        a-4
    else:
        print("0")
    if a > 1:
        print("1")
        a-2
    else:
        print("0")
    if a > 0:
        print("1")
        a-1
    else:
        print("0")
    print(".")

if b > 255:
    print("nesmí být více jak 255")
else:
    if b > 127:
        print("1")
        b-128
    else:
        print("0")
    if b > 63:
        print("1")
        b-64
    else:
        print("0")
    if b > 31:
        print("1")
        b-32
    else:
        print("0")
    if b > 15:
        print("1")
        b-16
    else:
        print("0")
    if b > 7:
        print("1")
        b-8
    else:
        print("0")
    if b > 3:
        print("1")
        b-4
    else:
        print("0")
    if b > 1:
        print("1")
        b-2
    else:
        print("0")
    if b > 0:
        print("1")
        b-1
    else:
        print("0")
    print(".")

if c > 255:
    print("nesmí být více jak 255")
else:
    if c > 127:
        print("1")
        c-128
    else:
        print("0")
    if c > 63:
        print("1")
        c-64
    else:
        print("0")
    if c > 31:
        print("1")
        c-32
    else:
        print("0")
    if c > 15:
        print("1")
        c-16
    else:
        print("0")
    if c > 7:
        print("1")
        c-8
    else:
        print("0")
    if c > 3:
        print("1")
        c-4
    else:
        print("0")
    if c > 1:
        print("1")
        c-2
    else:
        print("0")
    if c > 0:
        print("1")
        c-1
    else:
        print("0")
    print(".")

if d > 255:
    print("nesmí být více jak 255")
else:
    if d > 127:
        print("1")
        d-128
    else:
        print("0")
    if d > 63:
        print("1")
        d-64
    else:
        print("0")
    if d > 31:
        print("1")
        d-32
    else:
        print("0")
    if d > 15:
        print("1")
        d-16
    else:
        print("0")
    if d > 7:
        print("1")
        d-8
    else:
        print("0")
    if d > 3:
        print("1")
        d-4
    else:
        print("0")
    if d > 1:
        print("1")
        d-2
    else:
        print("0")
    if d > 0:
        print("1")
        d-1
    else:
       print("0")
