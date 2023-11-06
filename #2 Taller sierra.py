#2 Taller Sierra ej 2
tarjetas = [
    ["1234567890", "1234", 10000],
    ["0987654321", "4321", 5000],
    ["5678901234", "5678", 20000]
]

numero_tarjeta = input("Ingrese el número de tarjeta: ")

tarjeta_valida = None
for tarjeta in tarjetas:
    if tarjeta[0] == numero_tarjeta:
        tarjeta_valida = tarjeta
        break

if tarjeta_valida is not None:
    clave = input("Ingrese la clave: ")


    if clave == tarjeta_valida[1]:
        if tarjeta_valida[2] >= 10000:
            monto_a_retirar = int(input("Ingrese el monto a retirar: "))

            if monto_a_retirar <= tarjeta_valida[2]:
                tarjeta_valida[2] -= monto_a_retirar

                print(f"Retire su dinero: ${monto_a_retirar}")
                print(f"Saldo restante en la tarjeta: ${tarjeta_valida[2]}")
            else:
                print("El monto a retirar es mayor que el saldo disponible.")
        else:
            print("El saldo en la tarjeta es insuficiente para realizar un retiro de $10,000.")
    else:
        print("La clave ingresada no es válida.")
else:
    print("El número de tarjeta no es válido.")

