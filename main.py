# Programa Fet per Matias Gabriel Bañeres Villalba
# Part 1
import os
import pickle
import random
import csv
from prettytable import PrettyTable
def Taula():
    targeta = {
        1 : 4836,
        2 : 8903,
        3 : 5751,
        4 : 9616,
        5 : 4979,
        6 : 1029,
        7 : 1879,
        8 : 4932,
        9 : 3464,
        10 : 3833,
        11 : 3562,
        12 : 5173,
        13 : 6398,
        14 : 9371,
        15 : 9666,
        16 : 4710,
        17 : 2818,
        18 : 7893,
        19 : 5303,
        20 : 6175,
        21 : 8652,
        22 : 6213,
        23 : 8916,
        24 : 8994,
    }
    # Creació de la taula de coordenades
    fitxer = open('dades.dat', 'wb')
    pickle.dump(targeta, fitxer)
    fitxer.close()
Taula() 
coordenada = random.randrange(1,24) # Número del 1 al 24 generat a l'atzar
fitxer = open("dades.dat","rb")
targeta = pickle.load(fitxer)
acces = False
num = 3
contador = 3
codi_correcte = targeta.get(coordenada)
for intent in range(num):
    contador = contador-1
    codiproporcionat = input("Codi de la coordenada " + str(coordenada) + ":\n")
    codiproporcionat = int(codiproporcionat)
    if codiproporcionat == codi_correcte:
        print("\nCodi correcte.\n")
        acces = True
        break
    elif contador == 1:
        print("Error, et queda " + str(contador) + " intent")
    elif contador == 0:
        print("Limit d'intents superat.")
    else:
        print("Error, et queden " + str(contador) + " intents")
fitxer.close()
if acces == True:
    # Creació de les funcións
    def obtenir_ultim_codi():
        try:
            fitxer = open("dades.txt", "r")
            linies = fitxer.readlines()
            if linies:
                ultima_linia = linies[-1]
                dades_ultim = ultima_linia.strip().split(',')
                return int(dades_ultim[0])
            else:
                return 0
            fitxer.close()
        except FileNotFoundError:
            return 0
    def encriptacio(contrasenya):
        encriptat = ""
        algoritme = [1, 3, 4, 2]
        index = 0
        for caracter in contrasenya:
            codi = ord(caracter)
            noucodi = (codi + algoritme[index % len(algoritme)])
            encriptat += chr(noucodi)
            index = (index + 1) % len(algoritme)
        return encriptat
    operaciocontinuar = False
    operaciocontinuar2 = True
    while operaciocontinuar==False:
        while operaciocontinuar2 == True:
            print("*"*20)
            print("\n1. Inserir nou codi\n2. Eliminar codi\n3. Llistat ordenar\n4. Exportar a CSV\n5. Sortir\n")
            print("*"*20)
            opcio=input("\nOpció: ")
            opcio = int(opcio)
            if opcio == 1:
                codi = obtenir_ultim_codi() + 1
                if codi == 1:
                    codi = 0
                    servei = "Servei"
                    login = "Login"
                    pwd = "PWD"
                    noucodi = [codi,servei,login,pwd]
                    fitxer = open("dades.txt","w")
                    fitxer.write(','.join(map(str, noucodi)) + '\n')
                    fitxer.close()
                    codi = 1
                fitxer = open("dades.txt","a")
                servei = input("Quin es el servei\n")
                login = input("Login\n")
                pwd = input("Password\n")
                pwd = encriptacio(pwd)
                noucodi = [codi,servei,login,pwd]
                fitxer = open("dades.txt","a")
                fitxer.write(','.join(map(str, noucodi)) + '\n')
                print("\nRegistre creat\n")
                fitxer.close()
                operaciocontinuar2 = True
            elif opcio == 2:
                codi_eliminar = int(input("Introdueix el codi a eliminar: "))
                fitxeroriginal = open("dades.txt", "r")
                linies = fitxeroriginal.readlines()
                fitxeroriginal.close()
                fitxernou = open("dadesnoves.txt","w")
                trobat = False
                for linia in linies:
                    dades = linia.strip().split(',')
                    if int(dades[0]) == codi_eliminar:
                        trobat = True
                if trobat:
                    for linia in linies:
                        dades = linia.strip().split(',')
                        if int(dades[0]) != codi_eliminar:
                            fitxernou.write(linia)
                    print("\nRegistre eliminat\n")
                    fitxernou.close()
                    os.remove("dades.txt")
                    os.rename("dadesnoves.txt","dades.txt")
                else:
                    print("\nNo s'ha trobat el registre\n")
                    fitxernou.close()
                operaciocontinuar2 = True
            elif opcio == 3:
                fitxer = open("dades.txt","r")
                linies = fitxer.readlines()
                if linies == 0:
                    print("No hi ha registres per mostrar\n")
                else:
                    # Faig servir ',' com a delimitador al dividir les capçaleres
                    cabeceras = [campo.strip() for campo in linies[0].split(',')]
                    # creo una instancia de PrettyTable amb les capçaleres
                    taula = PrettyTable(cabeceras)
                    # Afegeixo les files de dades a la taula
                    for linia in linies[1:]:
                        taula.add_row([campo.strip() for campo in linia.split(',')])
                    # imprimo la taula
                    print(taula)
                fitxer.close()
                operaciocontinuar2 = True
            elif opcio == 4:
                try:
                    fitxer = open("dades.txt","r")
                    linies = fitxer.readlines()
                    fitxer.close()
                    fitxercsv = open('dades.csv', 'a')
                    writer = csv.writer(fitxercsv)
                    for line in linies:
                        fitxercsv.write(','.join([field.strip() for field in line.split(';')]) + '\n')
                    fitxercsv.close()
                except FileNotFoundError:
                    print("No hi han dades per exportar")
                operaciocontinuar2 = True
            elif opcio == 5:
                exit()
            else:
                print("Opció incorrecta")
                operaciocontinuar2 = True
                # case 4:
                # case 5: