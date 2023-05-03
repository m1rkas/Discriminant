import math

restart = "Yes"

while restart.lower() == "yes" or restart.lower() == "y" or restart == "":
    # input numbers of quadratic equation
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))

    # finding if b positive or negative
    if b > 0:
        symbolb = "+"
    elif b < 0:
        symbolb = "-"

    # finding if c positive or negative
    if c > 0:
        symbolc = "+"
        cd = c
    elif c < 0:
        cd = -c
        symbolc = "-"

    # finding Descriminant and if Descrominant positive or negative
    D = b**2 - 4*a*c
    if (-4*a*c) > 0:
        symbolD = "+"
        four = -4
    else:
        four = 4
        symbolD = "-"
    print("D =", str(b) + "²", "-4*" +str(a) + "*" + str(c), "=", b**2, symbolD, four*a*c, "=", D)

    # If descriminant < 0
    if D < 0:
        print("x є ∅")
    # if descriminant = 0
    elif D == 0:
        x = -b / (2*a)
        if x > 0:
            symbolx = "-"
            xd = x
        elif x < 0:
            symbolx = "+"
            xd = -x
        print("x =", -b, "/ (2*" + str(a) + ") =", -b, "/", 2*a, "=", x)
        print(str(a) + "x²", symbolb, str(b) + "x", symbolc, str(cd), "= (x", symbolx, str(xd) + ")²")
    # If descriminant > 0 and the root of descriminant is an integar number
    elif math.sqrt(D) == int(math.sqrt(D)):
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        if x1 > 0:
            symbolx1 = "-"
            xd1 = x1
        elif x1 < 0:
            symbolx1 = "+"
            xd1 = -x1
        if x2 > 0:
            symbolx2 = "-"
            xd2 = x2
        elif x2 < 0:
            symbolx2 = "+"
            xd2 = -x2
        print("x1 = (" + str(-b), "+ √" + str(D) + ") / (2*" + str(a) + ") = (" + str(-b), "+", str(int(math.sqrt(D))) + ") /", 2*a, "=" , -b + math.sqrt(D), "/", 2*a, "=", x1)
        print("x2 = (" + str(-b), "- √" + str(D) + ") / (2*" + str(a) + ") = (" + str(-b), "-", str(int(math.sqrt(D))) + ") /", 2*a, "=" , -b - math.sqrt(D), "/", 2*a, "=", x2,)
        print(str(a) + "x²", symbolb, str(b) + "x", symbolc, str(cd), "= (x", symbolx1, str(xd1) + ")(x", symbolx2, str(xd2) + ")")
    # If descriminant > 0 and the root of descriminant is NOT an integar number
    else:
        print("x1 =", str(-b) + "+√" + str(D), "/", 2*a)
        print("x2 =", str(-b) + "-√" + str(D), "/", 2*a)
        print(str(a) + "x²", symbolb, str(b) + "x", symbolc, str(cd), "= (x", str(-b) + "+√" + str(D) + "/" + str(2*a) +")(x", str(-b) + "-√" + str(D) + "/" + str(2*a) + ")")
    restart = input("Again?(Y/N): ")

