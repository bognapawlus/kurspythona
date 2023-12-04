import sys
import argparse
import wersja1

parser = argparse.ArgumentParser()
parser.add_argument("n", help="liczba ulamkow")
parser.add_argument("k", help="liczba dodawan")
parser.add_argument("w", help="wersja 1 lub 2")

args = parser.parse_args()

l = []
for i in range(int(args.n)):
    licz = i % 61 
    mian = (1000001 - i) % 31
    if mian == 0:
        mian = 1
    if int(args.w) == 2:
    	l.append(wersja2.Ulamek(licz, mian))
    else:
    	l.append(wersja1.Ulamek(licz, mian))

if int(args.w) == 2:
	s = wersja2.Ulamek(0, 1)
else:
	s = wersja1.Ulamek(0, 1)
	
for i in range(int(args.k)):
    s += l[i % int(args.n)]
print(s)

