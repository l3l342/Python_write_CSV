import sys

#zugriff
try:
    d = open("daten.csv", "w")

except:
    print("zugriff fehlgeschlagen")
    sys.exit(0)

#schreiben einer liste als csv datensatz
li = [42, "meier", 3542.65]

d.write(str(li[0]) + ";" + li[1] + ";" + str(li[2]).replace(".", ",") + "\n")


#zwei dimensionale liste
dli = [[55, "aslf", 3125], [75, "wasman", 2345.77]]

for element in dli:
    d.write(str(element[0]) + ";" + element[1] + ";" + str(element[2]).replace(".", ",") + "\n")

#schließen
d.close()
