
def main():
    edad = int(input("Ingresa tu edad: "))
    #Aquí empieza tu programa...
    if edad < 18 and edad > 0:
        print("No cumples requisitos")
    elif edad <= 0:
            print("Respuesta incorrecta")
    else:
        identificacion = str(input("¿Tienes identificación oficial? (s/n): "))
        
        if identificacion != "s" and identificacion != "n":
            print("Respuesta incorrecta")
        elif edad >= 18 and identificacion == "s":
            print("Trámite de licencia concedido")
        else:
            print("No cumples requisitos")

if __name__ == '__main__':
    main()
