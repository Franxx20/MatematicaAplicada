def CaesarCipher():
    alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
    

    mensaje = input("Enter your mensaje: ")
    print(mensaje)


    shift = int(input("Enter the shift: "))
    print(shift)

    mensaje = mensaje.lower()
    resultado = ""


    for letra in mensaje:
        if letra in alfabeto:
            indice = alfabeto.find(letra)

            indice = (indice + shift)%(len(alfabeto))

            # si el indice es mayor al tamanio del abacedario o menor a 0 
            if indice < 0:
                indice = indice + len(alfabeto)

            resultado = resultado + alfabeto[indice]

        else:
            resultado = resultado + letra


    return resultado


print("Mensaje Encriptado: "+ CaesarCipher())
