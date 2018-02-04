# Programma che effettua una trasformazione gamma all'immagine passata in input
#   s = c * r^y
# Usage: python3 gamma.py [c] [y] [image.pgm]

import sys

    # Ottengo informazioni dai parametri argv
c = int(sys.argv[1])
y = int(sys.argv[2])
f_in = open(sys.argv[3], 'r')

    # Ottengo dati da immagine sorgente
format = f_in.readline()
editor = f_in.readline()
dim = f_in.readline()

list = dim.split(" ")

h = int(list[0])        # pixel altezza
b = int(list[1])        # pixel larghezza
max = int(f_in.readline()) # massimo valore del pixel

    # Creo nuova immagine
newfile = str(c)+"gamma"+str(y)+(sys.argv[3])
f_out = open(newfile, 'w')

f_out.write(format)
f_out.write(editor)
f_out.write(dim)
f_out.write(str(max)+"\n")
for line in f_in:
    pixel = int(line)
    newpixel = c * pixel**y
    if (newpixel > max):
        newpixel = int((newpixel * max) / (max**y))
    f_out.write(str(newpixel)+"\n")

print("trasformazione completata !")

    
    
    
