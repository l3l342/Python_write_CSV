import sys

#zugriff
try:
    d = open("daten.csv")
except:
    print("fehlgeschlagen")
    sys.exit(0)

#lesen des gesamten text
gesamtertext = d.read()

#schliessen der datei
d.close()

#umwandeln in eine liste
zeilenliste = gesamtertext.split(chr(10))

#jede zeile umwandeln in liste von int float und string
li = []
for zeile in zeilenliste:
    if zeile:
        zwliste = zeile.split(";")
        li.append([int(zwliste[0]),zwliste[1], float(zwliste[2].replace(",", "."))])

#ausgabe
for p in li:
    print(f"{p[0]:d} {p[1]} {p[2]:.2f}")
