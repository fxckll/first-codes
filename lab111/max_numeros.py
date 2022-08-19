# imprimir el mayor numero 
a,b,c = map(int,input().split())
if a >= b and a >= c:
    print(f"{a}")
elif b >= a and b >= c:
    print(f"{b}")
elif c >= a and c >= b:
    print(f"{c}")