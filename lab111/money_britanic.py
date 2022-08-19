import sys
for p in sys.stdin: # para leer datos externos TXT
    n = int(p)      # ver la entrada de datos
    libras = (n/12)/20
    chelin = (n/12)%20
    ex = chelin - int(chelin)
    penique = round(ex * 12)
    l = int(libras)
    c = int(chelin)
    print(f"({l}, {c}, {penique})")