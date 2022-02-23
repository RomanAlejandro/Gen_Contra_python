# GENERADOR DE CONTRASEÑAS
# ROMAN ALEJANDRO GM

# CARACTERES
import random

letras_minusculas= "abcdefghijklmnopqrstuvwxyz"
letras_mayusculas= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros= "0123456789"
simbolos= "$#-*(){}[]"

todo_los_caracteres = letras_minusculas+letras_mayusculas+numeros+simbolos
tamaño = 16

print("\n\n\t█▀▀ █▀▀ █▄░█ █▀▀ █▀█ ▄▀█ █▀▄ █▀█ █▀█")
print("\t█▄█ ██▄ █░▀█ ██▄ █▀▄ █▀█ █▄▀ █▄█ █▀▄")
print("")
print("\t█▀▄ █▀▀")
print("\t█▄▀ ██▄")
print("\t                                 ▄▄")
print("\t█▀▀ █▀█ █▄░█ ▀█▀ █▀█ ▄▀█ █▀ █▀▀ █▄░█ ▄▀█ █▀")
print("\t█▄▄ █▄█ █░▀█ ░█░ █▀▄ █▀█ ▄█ ██▄ █░▀█ █▀█ ▄█")

while True:
###############################################################################
    # CUANTAS CONTRASEÑAS OCUPAS
    tcontraseñas = int(input("\n\n\t ¿CUANTAS CONTRASEÑAS OCUPAS? : "))
    while (tcontraseñas <= 0):
        print("\n\n\tUPSSS creo que no ingresaste un valor valido")
        tcontraseñas = int(input("\n\n\t ¿CUANTAS CONTRASEÑAS OCUPAS? : "))
        

###############################################################################
    # TAMAÑO NUEVO DE LA CONTRASEÑA
    print("\n\n\tEL TAMAÑO PREDETERMINADO SERA DE 16 CARACTERES")
    desicion = input("\n\t ¿QUIERES DEFINIR UN TAMAÑO A LA CONTRASEÑA? (si/no) : ")
    if(desicion=="Si") or (desicion=="SI") or (desicion=="si"):
        tamaño_nuevo = int(input("\n\n\t TAMAÑO : "))
        while (tamaño_nuevo <= 0) or (tamaño_nuevo >= 64):
            print("\n\n\tUPSSS creo que no ingresaste un valor valido o esta muy alto")
            tamaño_nuevo = int(input("\n\n\t TAMAÑO : "))
        if (tcontraseñas > 0):
            for i in range(tcontraseñas):
                contraseña = "".join(random.sample(todo_los_caracteres,tamaño_nuevo))
                print("\tTU CONTRASEÑA ES : ",contraseña)

            
    else:
        print("\n\n\tOK - EL TAMAÑO DE LA CONTRASEÑA SERA DE 16 CARACTERES")

        
###############################################################################
    # PROCESO CON TAMAÑO DE CONTRASEÑA PREDETERMINADA
        if (tcontraseñas > 0):
            for i in range(tcontraseñas):
                contraseña = "".join(random.sample(todo_los_caracteres,tamaño))
                print("\tTU CONTRASEÑA ES : ",contraseña)
            






