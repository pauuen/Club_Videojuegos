from colorama import Fore, Back, Style
nombrec=[]
gamertag=[]
edadc=[]
gamec=[]
while True:
    print(f"{Fore.RED}1.-Alta de nuevos miembros en el club.")
    print("2.-Baja de un miembro que desee salir del club.")
    print("3.-Modificación de un miembro")
    print("4.-Consulta de miembro del club")
    print(f"5.-Salir {Style.RESET_ALL}")
    opc=int(input(f"Elige la opcion a realizar: "))
    if (opc == 1):
        nombre=input(f"{Fore.YELLOW}Ingrese nombre: ")
        nombrec.append(nombre)
        edad=input(f"Ingrese edad: ")
        edadc.append(edad)
        game=input(f"Ingrese su gamertag: ")
        gamertag.append(game)
        vid=input(f"Ingrese su videojuego favorito: ")
        gamec.append(vid)
        print(f"¡Miembro agregado exitosamente!{Style.RESET_ALL}")
    if (opc == 2):
        nombre=input(f"{Fore.MAGENTA}Dame el nombre del miembro para darlo de baja: ")
        if (nombre in nombrec):
            ind=nombrec.index(nombre)
            nombrec.pop(ind)
            gamertag.pop(ind)
            edadc.pop(ind)
            gamec.pop(ind)
            print("la base de datos del club actualizada ",nombrec,gamertag,edadc,gamec)
        else:
            print(f"",nombre, " no esta en la lista{Style.RESET_ALL}")
    if (opc == 3):
        nombre=input(f"{Fore.BLUE}Dame el nombre del miembro para cambiar sus datos: ")
        if (nombre in nombrec):
            ind=nombrec.index(nombre)
            print(f"1.- Cambiar su gamertag")
            print("2.- Cambiar su videojuego favorito")
            opc2 = int(input("Elige la opción a realizar: "))
            if opc2 == 1:
                new = input("Dame el nuevo gamertag: ")
                gamertag[ind] = new
            if opc2 == 2:
                new = input("Dame el nuevo videojuego favorito: ")
                gamec[ind] = new
            else:
                print(f"{Fore.BLUE}Opción inválida.{Style.RESET_ALL}")
        else:
            print(f"{Fore.BLUE}Opción inválida.{Style.RESET_ALL}")        
    if (opc == 4):
        nombre=input(f"{Fore.CYAN}Dame el nombre del miembro para obtener sus datos:")
        if nombre in nombrec:
            ind=nombrec.index(nombre)
            print(f"Su gamertag es: {gamertag[ind]}")
            print(f"Su edad es: {edadc[ind]}")
            print(f"Su videojuego favorito es: {gamec[ind]}")
        else:
            print(f"El usuario no se encuentra{Style.RESET_ALL}")
    if (opc == 5):
        print(f"{Fore.RED}¡Gracias por venir vuelva pronto!{Style.RESET_ALL}")
        break
