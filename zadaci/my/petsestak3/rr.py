import argparse
from ravnina import Tocka,Vektor
import sys
from IPython.core import ultratb
import pdb

parser = argparse.ArgumentParser(description='Proslijedite vektore.')
parser.add_argument('u_dvojke', metavar='(X,Y)', type=str, nargs=2,
                   help='vektor zapisan kao uredjena dvojka')
parser.add_argument('--add', dest='accumulate', action='store_const',
                    const=Vektor.__add__,
                   help='zbrajanje vektora')
parser.add_argument('--sub', dest='accumulate', action='store_const',
                    const=Vektor.__sub__,
                   help='oduzimanje vektora')
parser.add_argument('--debug', action='store_true', dest='debug', #makar bi se ionako varijabla (točnije atribut) koja sadrzava vrijednost ovog argumenata imala taj naziv ('debug') jer bi se sa početno definirane zastavice zanemarile vodeće crtice (jer varijable moraju početi slovom ili underscoreom)
                    help='pokretanje debug nacina rada')
parser.add_argument('--verbose', action='store_true', #ovdje nije eksplicitno navedeno da će naziv varijable (atributa) biti "verbose", pa će se svejedno tamo spremati True (ako će biti argument proslijeđen)
                    help='pokretanje verbose nacina rada')

args = parser.parse_args()
if args.debug==True:
    pdb.set_trace()
if args.verbose==True:
    sys.excepthook = ultratb.FormattedTB(mode='Verbose',
    color_scheme='Linux', call_pdb=1)
#print(args.integers)
#vektori=args.integers.strip(" ")
for i in range (0,len(args.u_dvojke)):
    args.u_dvojke[i]=args.u_dvojke[i].replace("(","").replace(")","")
    args.u_dvojke[i]=args.u_dvojke[i].split(",")
    args.u_dvojke[i]=[int(x) for x in args.u_dvojke[i]]
    args.u_dvojke[i]=Vektor(args.u_dvojke[i][0],args.u_dvojke[i][1])
#print(args.integers)
print(args.accumulate(args.u_dvojke[0],args.u_dvojke[1]))
#print(args.accumulate(args.integers))