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