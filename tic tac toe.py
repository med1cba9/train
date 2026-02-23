posi = {"13": "-", "23": "-", "33": "-",
        "12": "-", "22": "-", "32": "-",
        "11": "-", "21": "-", "31": "-"}

class lines:
    def _1x(self):
        if (posi["11"] == posi["22"] == posi["33"]):
            return 1
        else:
            return 0

    def _y1(self):
        if (posi["11"] == posi["21"] == posi["31"]):
            return 1
        else:
            return 0

    def _x1(self):
        if (posi["11"] == posi["12"] == posi["13"]):
            return 1
        else:
            return 0


    def _y2(self):
        if (posi["12"] == posi["22"] == posi["32"]):
            return 1
        else:
            return 0

    def _x2(self):
        if (posi["21"] == posi["22"] == posi["23"]):
            return 1
        else:
            return 0

    def _nx(self):
        if (posi["13"] == posi["22"] == posi["31"]):
            return 1
        else:
            return 0


    def _y3(self):
        if (posi["13"] == posi["23"] == posi["33"]):
            return 1
        else:
            return 0

    def _x3(self):
        if (posi["31"] == posi["32"] == posi["33"]):
            return 1
        else:
            return 0

check = lines()

def display():
    print("")
    print(f"3 |{posi["13"]}| |{posi["23"]}| |{posi["33"]}|")
    print(f"2 |{posi["12"]}| |{posi["22"]}| |{posi["32"]}|")
    print(f"1 |{posi["11"]}| |{posi["21"]}| |{posi["31"]}|")
    print("   1   2   3")
    print("")


def range_checker(a, b):
    if not (1 <= int(a) <= 3 and 1<= int(b) <= 3):  # abnormal input
        return 1
    else:
        return 0

def line_checker(tgt):  # target
    if (posi["11"] == tgt):
        cs = [0, 0, 0]  # checksum
        cs[0] = check._1x()
        cs[1] = check._y1()
        cs[2] = check._x1()
        return 0 if sum(cs) == 0 else 1

    if (posi["22"] == tgt):
        cs = [0, 0, 0]
        cs[0] = check._y2()
        cs[1] = check._x2()
        cs[2] = check._nx()
        return 0 if sum(cs) == 0 else 1

    if (posi["33"] == tgt):
        cs = [0, 0, 0]
        cs[0] = check._y3()
        cs[1] = check._x3()
        return 0 if sum(cs) == 0 else 1


def game(side):
    while True:
        stopper = 0
        x, y = input(f"{side}: ")
        dic_key = x + y

        stopper = range_checker(x, y)
        if (stopper == 1):
            print("Input out of range. Try again")
            continue

        elif not (posi[dic_key] == "-"):
            print("Position already taken. Try again")

        else:
            posi[dic_key] = side

            if (line_checker(side) == 1):
                display()
                print(f"{side} won")
                return -1

            display()
            break

display()
print("input instance: 12 for coordinate (1, 2)")
print("")

while True:
    if game("O") == -1:
        break
    if game("X") == -1:
        break











