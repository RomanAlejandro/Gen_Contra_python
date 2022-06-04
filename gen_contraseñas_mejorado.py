# GENERADOR DE CONTRASEÑAS
# ROMAN ALEJANDRO GM

# CARACTERES
import random
import os
os.system('color 0a')
letras_minusculas= "abcdefghijklmnñopqrstuvwxyz"
letras_mayusculas= "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
numeros= "0123456789"
simbolos= "$#-*(){}[]"

todo_los_caracteres = letras_minusculas+letras_mayusculas+numeros+simbolos
tamaño = 16
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("""

    ▒█▀▀█ █▀▀ █▀▀▄ █▀▀ █▀▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀█ 
    ▒█░▄▄ █▀▀ █░░█ █▀▀ █▄▄▀ █▄▄█ █░░█ █░░█ █▄▄▀
    ▒█▄▄█ ▀▀▀ ▀░░▀ ▀▀▀ ▀░▀▀ ▀░░▀ ▀▀▀░ ▀▀▀▀ ▀░▀▀


       █▀▀▄ █▀▀    █▓▒▓█▀██▀█▄░░▄█▀██▀█▓▒▓█
       █░░█ █▀▀    █▓▒░▀▄▄▄▄▄█░░█▄▄▄▄▄▀░▒▓█
       ▀▀▀░ ▀▀▀    █▓▓▒░░░░░▒▓░░▓▒░░░░░▒▓▓█
   
                                      ▀▀▀
█▀▀ █▀▀█ █▀▀▄ ▀▀█▀▀ █▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀▄ █▀▀█ █▀▀    ▄ ▒█▀▀▄ 
█░░ █░░█ █░░█ ░░█░░ █▄▄▀ █▄▄█ ▀▀█ █▀▀ █░░█ █▄▄█ ▀▀█    ░ ▒█░▒█ 
▀▀▀ ▀▀▀▀ ▀░░▀ ░░▀░░ ▀░▀▀ ▀░░▀ ▀▀▀ ▀▀▀ ▀░░▀ ▀░░▀ ▀▀▀    ▀ ▒█▄▄▀

""")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
while True:
###############################################################################
    # CUANTAS CONTRASEÑAS OCUPAS
    tcontraseñas = int(input("\n\n\t ¿CUANTAS CONTRASEÑAS OCUPAS? : "))
    while (tcontraseñas <= 0):
        print("\n\n\t UPSSS creo que no ingresaste un valor valido")
        tcontraseñas = int(input("\n\n\t ¿CUANTAS CONTRASEÑAS OCUPAS? : "))

    contador = 0
###############################################################################
    # TAMAÑO NUEVO DE LA CONTRASEÑA
    print("\n\n\t EL TAMAÑO PREDETERMINADO SERA DE 16 CARACTERES")
    desicion = input("\n\t ¿QUIERES DEFINIR UN TAMAÑO A LA CONTRASEÑA? (si/no) : ")
    if(desicion=="Si") or (desicion=="SI") or (desicion=="si") or (desicion=="s")  or (desicion=="sI") or (desicion=="1"):
        tamaño_nuevo = int(input("\n\n\t TAMAÑO : "))
        while (tamaño_nuevo <= 0) or (tamaño_nuevo > 70):
            print("\n\n\t UPSSS creo que no ingresaste un valor valido o esta muy alto")
            tamaño_nuevo = int(input("\n\n\t TAMAÑO : "))
        if (tcontraseñas > 0):
            for i in range(tcontraseñas):
                contraseña = "".join(random.sample(todo_los_caracteres,tamaño_nuevo))
                contador+=1
                print("\t [",contador,"]","TU CONTRASEÑA ES : ",contraseña)

            
    else:
        print("\n\n\tOK - EL TAMAÑO DE LA CONTRASEÑA SERA DE 16 CARACTERES")

        
###############################################################################
    # PROCESO CON TAMAÑO DE CONTRASEÑA PREDETERMINADA
        if (tcontraseñas > 0):
            for i in range(tcontraseñas):
                contraseña = "".join(random.sample(todo_los_caracteres,tamaño))
                contador+=1
                print("\t [",contador,"]","TU CONTRASEÑA ES : ",contraseña)
