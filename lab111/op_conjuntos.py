while True:         #este funciona no como el otro jajajaxd
    try:
        a,b = map(int,input().split())  
        c = a | b
        d = a & b
        e = c ^ b
        print(f"{c} {d} {e}")
    except EOFError:
        break