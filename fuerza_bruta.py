from string import ascii_lowercase
from getpass import getpass

password = getpass("Ingrese la contraseña ").lower()

contador = 0

for i in password:
    for letra2 in ascii_lowercase:
        if i == letra2:
            contador += 1
            break
        else:
            contador += 1
        
print(f"{contador} intentos")