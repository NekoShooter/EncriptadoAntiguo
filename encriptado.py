def LlaveDe_Encriptado(Llave):
    LlaveDe_Seguridad = []
    for letra in Llave:
        LlaveDe_Seguridad.append(ord(letra))
    return LlaveDe_Seguridad

# ASCII 32 al 126 <- Por comodidad no mas
def emparejar(letra_Original,Llave):
    base_numerica = ord(letra_Original) + Llave
    while base_numerica > 126:
        base_numerica = (base_numerica - 126) + 32    
    return chr(base_numerica)

def desemparejar(Letra_cifrada, Llave):
    base_numerica = ord(Letra_cifrada) - Llave
    while base_numerica < 32:
        base_numerica = (base_numerica + 126) - 32
    
    return chr(base_numerica)


def Procesar_Mensaje(mensaje,Llave,opcion):
    LlaveDe_Cifrado = LlaveDe_Encriptado(Llave)
    dimencion = len(LlaveDe_Cifrado) - 1
    indice = 0
    Procesado_completo = []
    Accion = {"Cifrar" : True, "Descifrar" : False}
    for letra in mensaje:
        if indice > dimencion:
            indice = 0
        if Accion[opcion]:
            Procesado_completo.append(emparejar(letra,LlaveDe_Cifrado[indice]))
        else:
            Procesado_completo.append(desemparejar(letra,LlaveDe_Cifrado[indice]))
        indice +=1
    return "".join(Procesado_completo)

if __name__ == "__main__":
    print("---ENIGMA primitiva---")
    while True:
        print("Que desea realizar \n")
        print("[C]ifrar\n[D]escifrar\n[S]alir\n\n")
        opcion = input("¿Cual es su elecion?\n>>> ")
        if opcion == 'c':
            mensaje = input("ingrese su mensaje \n>>> ")
            LlaveDe_Seguridad = input("ingrese una contraseña para cifrar\n<<< ")
            cifrado = Procesar_Mensaje(mensaje,LlaveDe_Seguridad,"Cifrar")
            print("cifrado\n>>> {}\n".format(cifrado))

        elif opcion =='d':
            mensaje = input("ingrese su mensaje \n>>> ")
            LlaveDe_Seguridad = input("ingrese su contraseña para descifrar\n<<< ")
            decifrar = Procesar_Mensaje(mensaje,LlaveDe_Seguridad,"Descifrar")
            print("descifrado\n>>> {}\n".format(decifrar))

        else:
            print("Proceso Terminado")
            break