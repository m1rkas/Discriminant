import math

restart = "Yes"

while restart.lower() == "yes" or restart.lower() == "y" or restart == "":
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))

    D = b**2 -4*a*c
    print("D =", D)

    if D < 0:
        print("x є ∅")
    elif D == 0:
        x = -b / (2*a)
        print("x =", -b, "/ (2*" + str(a) + ") =", -b, "/", 2*a, "=", x)
    elif math.sqrt(D) == int(math.sqrt(D)):
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print("x1 = (" + str(-b), "+ √" + str(D) + ") / (2*" + str(a) + ") = (" + str(-b), "+", str(int(math.sqrt(D))) + ") /", 2*a, "=" , -b + math.sqrt(D), "/", 2*a, "=", x1)
        print("x2 = (" + str(-b), "- √" + str(D) + ") / (2*" + str(a) + ") = (" + str(-b), "-", str(int(math.sqrt(D))) + ") /", 2*a, "=" , -b - math.sqrt(D), "/", 2*a, "=", x2)
    else:
        print("x1 =", str(-b) + "+√" + str(D), "/", 2*a)
        print("x2 =", str(-b) + "-√" + str(D), "/", 2*a)
    restart = input("Again?(Y/N): ")

