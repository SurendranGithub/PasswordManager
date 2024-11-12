def encode(org):
    encoded = ""
    for i in range(len(org)):
        if org[i]=='A':
            encoded+='D'
        elif org[i]=='B':
            encoded+='N'
        elif org[i]=='C':
            encoded+='T'
        elif org[i]=='D':
            encoded+='J'
        elif org[i]=='E':
            encoded+='Q'
        elif org[i]=='F':
            encoded+='W'
        elif org[i]=='G':
            encoded+='P'
        elif org[i]=='H':
            encoded+='F'
        elif org[i]=='I':
            encoded+='X'
        elif org[i]=='J':
            encoded+='Z'
        elif org[i]=='K':
            encoded+='A'
        elif org[i]=='L':
            encoded+='E'
        elif org[i]=='M':
            encoded+='V'
        elif org[i]=='N':
            encoded+='S'
        elif org[i]=='O':
            encoded+='C'
        elif org[i]=='P':
            encoded+='H'
        elif org[i]=='Q':
            encoded+='M'
        elif org[i]=='R':
            encoded+='G'
        elif org[i]=='S':
            encoded+='U'
        elif org[i]=='T':
            encoded+='L'
        elif org[i]=='U':
            encoded+='Y'
        elif org[i]=='V':
            encoded+='R'
        elif org[i]=='W':
            encoded+='I'
        elif org[i]=='X':
            encoded+='O'
        elif org[i]=='Y':
            encoded+='B'
        elif org[i]=='Z':
            encoded+='K'
        elif org[i]=='a':
            encoded+='d'
        elif org[i]=='b':
            encoded+='n'
        elif org[i]=='c':
            encoded+='t'
        elif org[i]=='d':
            encoded+='j'
        elif org[i]=='e':
            encoded+='q'
        elif org[i]=='f':
            encoded+='w'
        elif org[i]=='g':
            encoded+='p'
        elif org[i]=='h':
            encoded+='f'
        elif org[i]=='i':
            encoded+='x'
        elif org[i]=='j':
            encoded+='z'
        elif org[i]=='k':
            encoded+='a'
        elif org[i]=='l':
            encoded+='e'
        elif org[i]=='m':
            encoded+='v'
        elif org[i]=='n':
            encoded+='s'
        elif org[i]=='o':
            encoded+='c'
        elif org[i]=='p':
            encoded+='h'
        elif org[i]=='q':
            encoded+='m'
        elif org[i]=='r':
            encoded+='g'
        elif org[i]=='s':
            encoded+='u'
        elif org[i]=='t':
            encoded+='l'
        elif org[i]=='u':
            encoded+='y'
        elif org[i]=='v':
            encoded+='r'
        elif org[i]=='w':
            encoded+='i'
        elif org[i]=='x':
            encoded+='o'
        elif org[i]=='y':
            encoded+='b'
        elif org[i]=='z':
            encoded+='k'
        else:
            encoded+=org[i]
    return encoded

def decode(org):
    decoded = ""
    for i in range(len(org)):
        if org[i]=='A':
            decoded+='K'
        elif org[i]=='B':
            decoded+='Y'
        elif org[i]=='C':
            decoded+='O'
        elif org[i]=='D':
            decoded+='A'
        elif org[i]=='E':
            decoded+='L'
        elif org[i]=='F':
            decoded+='H'
        elif org[i]=='G':
            decoded+='R'
        elif org[i]=='H':
            decoded+='P'    
        elif org[i]=='I':
            decoded+='W'
        elif org[i]=='J':
            decoded+='D'
        elif org[i]=='K':
            decoded+='Z'
        elif org[i]=='L':
            decoded+='T'
        elif org[i]=='M':
            decoded+='Q'
        elif org[i]=='N':
            decoded+='B'
        elif org[i]=='O':
            decoded+='X'
        elif org[i]=='P':
            decoded+='G'
        elif org[i]=='Q':
            decoded+='E'
        elif org[i]=='R':
            decoded+='V'
        elif org[i]=='S':
            decoded+='N'
        elif org[i]=='T':
            decoded+='C'
        elif org[i]=='U':
            decoded+='S'
        elif org[i]=='V':
            decoded+='M'
        elif org[i]=='W':
            decoded+='F'
        elif org[i]=='X':
            decoded+='I'
        elif org[i]=='Y':
            decoded+='U'
        elif org[i]=='Z':
            decoded+='J'
        elif org[i]=='a':
            decoded+='k'
        elif org[i]=='b':
            decoded+='y'
        elif org[i]=='c':
            decoded+='o'
        elif org[i]=='d':
            decoded+='a'
        elif org[i]=='e':
            decoded+='l'
        elif org[i]=='f':
            decoded+='h'
        elif org[i]=='g':
            decoded+='r'
        elif org[i]=='h':
            decoded+='p'
        elif org[i]=='i':
            decoded+='w'
        elif org[i]=='j':
            decoded+='d'
        elif org[i]=='k':
            decoded+='z'
        elif org[i]=='l':
            decoded+='t'
        elif org[i]=='m':
            decoded+='q'
        elif org[i]=='n':
            decoded+='b'
        elif org[i]=='o':
            decoded+='x'
        elif org[i]=='p':
            decoded+='g'
        elif org[i]=='q':
            decoded+='e'
        elif org[i]=='r':
            decoded+='v'
        elif org[i]=='s':
            decoded+='n'
        elif org[i]=='t':
            decoded+='c'
        elif org[i]=='u':
            decoded+='s'
        elif org[i]=='v':
            decoded+='m'
        elif org[i]=='w':
            decoded+='f'
        elif org[i]=='x':
            decoded+='i'
        elif org[i]=='y':
            decoded+='u'
        elif org[i]=='z':
            decoded+='j'
        else:
            decoded+=org[i]
    return decoded

a = "abcdefghijklmnopqrstuvwxyz"
print(decode("qwer"))
