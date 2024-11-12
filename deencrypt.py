def decode1(orgl):
    de = ""
    leng = len(orgl)
    org = ""
    for i in range(leng):
        if i % 2 == 0:
            org += chr(ord(orgl[i]) - leng//2)
        else:
            org += chr(ord(orgl[i]) + leng//2)
    if org[-3:] == '128':
        fir = '₹'
    else:
        fir = chr(int(org[-3:]))
    orgi = fir + org[0:leng-3]

    for i in orgi:
        if i == "A":
            de += "G"
        elif i == "B":
            de += "d"
        elif i == "C":
            de += "P"
        elif i == "D":
            de += "+"
        elif i == "E":
            de += "k"
        elif i == "F":
            de += "~"
        elif i == "G":
            de += "-"
        elif i == "H":
            de += "1"
        elif i == "I":
            de += "C"
        elif i == "J":
            de += "9"
        elif i == "K":
            de += "Y"
        elif i == "L":
            de += "s"
        elif i == "M":
            de += "2"
        elif i == "N":
            de += "L"
        elif i == "O":
            de += "r"
        elif i == "P":
            de += "@"
        elif i == "Q":
            de += "8"
        elif i == "R":
            de += "I"
        elif i == "S":
            de += "o"
        elif i == "T":
            de += "X"
        elif i == "U":
            de += "Z"
        elif i == "V":
            de += "e"
        elif i == "W":
            de += "B"
        elif i == "X":
            de += "₹"
        elif i == "Y":
            de += "O"
        elif i == "Z":
            de += "_"


        elif i == "a":
            de += "W"
        elif i == "b":
            de += "v"
        elif i == "c":
            de += "*"
        elif i == "d":
            de += "0"
        elif i == "e":
            de += "q"
        elif i == "f":
            de += "^"
        elif i == "g":
            de += "K"
        elif i == "h":
            de += "v"
        elif i == "i":
            de += "f"
        elif i == "j":
            de += "A"
        elif i == "k":
            de += "3"
        elif i == "l":
            de += "a"
        elif i == "m":
            de += "g"
        elif i == "n":
            de += "E"
        elif i == "o":
            de += "U"
        elif i == "p":
            de += "#"
        elif i == "q":
            de += "'"
        elif i == "r":
            de += "z"
        elif i == "s":
            de += "!"
        elif i == "t":
            de += "%"
        elif i == "u":
            de += "y"
        elif i == "v":
            de += "T"
        elif i == "w":
            de += "&"
        elif i == "x":
            de += "p"
        elif i == "y":
            de += "$"
        elif i == "z":
            de += "h"
        
        elif i == "+":
            de += "j"
        elif i == "-":
            de += "N"
        elif i == "/":
            de += " "
        elif i == "*":
            de += "u"
        elif i == "@":
            de += "m"
        elif i == "₹":
            de += "S"
        elif i == "$":
            de += "/"
        elif i == "^":
            de += "i"
        elif i == "%":
            de += "H"
        elif i == "#":
            de += "b"
        elif i == "!":
            de += "D"
        elif i == "'":
            de += "w"
        elif i == "~":
            de += "J"
        elif i == "&":
            de += "7"


        elif i == "1":
            de += "n"
        elif i == "2":
            de += "R"
        elif i == "3":
            de += "M"
        elif i == "4":
            de += "c"
        elif i == "5":
            de += "l"
        elif i == "6":
            de += "Q"
        elif i == "7":
            de += "5"
        elif i == "8":
            de += "x"
        elif i == "9":
            de += "t"
        elif i == "0":
            de += "F"

        elif i == "_":
            de += "4"
        elif i == " ":
            de += "6"
        else:
            de += i

    return de

def encode1(org):
    en = ""
    for i in org:
        if i == "G":
            en += "A"
        elif i == "d":
            en += "B"
        elif i == "P":
            en += "C"
        elif i == "+":
            en += "D"
        elif i == "k":
            en += "E"
        elif i == "~":
            en += "F"
        elif i == "-":
            en += "G"
        elif i == "1":
            en += "H"
        elif i == "C":
            en += "I"
        elif i == "9":
            en += "J"
        elif i == "Y":
            en += "K"
        elif i == "s":
            en += "L"
        elif i == "2":
            en += "M"
        elif i == "L":
            en += "N"
        elif i == "r":
            en += "O"
        elif i == "@":
            en += "P"
        elif i == "8":
            en += "Q"
        elif i == "I":
            en += "R"
        elif i == "o":
            en += "S"
        elif i == "X":
            en += "T"
        elif i == "Z":
            en += "U"
        elif i == "e":
            en += "V"
        elif i == "B":
            en += "W"
        elif i == "₹":
            en += "X"
        elif i == "O":
            en += "Y"
        elif i == "_":
            en += "Z"


        elif i == "W":
            en += "a"
        elif i == "v":
            en += "b"
        elif i == "*":
            en += "c"
        elif i == "0":
            en += "d"
        elif i == "q":
            en += "e"
        elif i == "^":
            en += "f"
        elif i == "K":
            en += "g"
        elif i == "V":
            en += "h"
        elif i == "f":
            en += "i"
        elif i == "A":
            en += "j"
        elif i == "3":
            en += "k"
        elif i == "a":
            en += "l"
        elif i == "g":
            en += "m"
        elif i == "E":
            en += "n"
        elif i == "U":
            en += "o"
        elif i == "#":
            en += "p"
        elif i == "'":
            en += "q"
        elif i == "z":
            en += "r"
        elif i == "!":
            en += "s"
        elif i == "%":
            en += "t"
        elif i == "y":
            en += "u"
        elif i == "T":
            en += "v"
        elif i == "&":
            en += "w"
        elif i == "p":
            en += "x"
        elif i == "$":
            en += "y"
        elif i == "h":
            en += "z"
        
        elif i == "j":
            en += "+"
        elif i == "N":
            en += "-"
        elif i == " ":
            en += "/"
        elif i == "u":
            en += "*"
        elif i == "m":
            en += "@"
        elif i == "S":
            en += "₹"
        elif i == "/":
            en += "$"
        elif i == "i":
            en += "^"
        elif i == "H":
            en += "%"
        elif i == "b":
            en += "#"
        elif i == "D":
            en += "!"
        elif i == "w":
            en += "'"
        elif i == "J":
            en += "~"
        elif i == "7":
            en += "&"


        elif i == "n":
            en += "1"
        elif i == "R":
            en += "2"
        elif i == "M":
            en += "3"
        elif i == "c":
            en += "4"
        elif i == "l":
            en += "5"
        elif i == "Q":
            en += "6"
        elif i == "5":
            en += "7"
        elif i == "x":
            en += "8"
        elif i == "t":
            en += "9"
        elif i == "F":
            en += "0"

        elif i == "4":
            en += "_"
        elif i == "6":
            en += " "
        else:
            en += i
    if en[0] == '₹':
        fir = '128'
    else:
        if ord(en[0]) < 100:
            fir = '0' + str(ord(en[0]))
        else:
            fir = str(ord(en[0]))
    dec = en[1:] + fir
    lengt = len(dec)
    encoded = ""
    for i in range(lengt):
        if i % 2 == 0:
            encoded += chr(ord(dec[i]) + lengt//2)
        else:
            encoded += chr(ord(dec[i]) - lengt//2)
    return encoded

# a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890+-/*@₹$^%#!'~& _"
# a = "zombie@1234.gmail.com"
# a1 = ""
# print(encode1(a))
# print(decode1(encode1(a)))
# print(len(a), "\t", len(decode1(encode1(a))), "\t", len(encode1(a)))