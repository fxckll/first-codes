# letra o numero
n = input()
v = ord(n)
if v >= 48 and v<= 57:
    print("Es numero.")
elif v >= 65 and v <= 90:
    print("Es letra mayúscula.")
elif v >= 97 and v <= 122:
    print("Es letra minúscula.") 
else:
    print("No es letra ni número.")