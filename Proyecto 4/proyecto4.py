#from termcolor import colored
from sys import stdout

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#print color.RED + 'Hello World !' + color.END
###############################################

print "1. Leer de un archivo"
print "2. Insertar Manual"
arOcmd = raw_input('Dame el numero de eleccion:  ')
arOcmd = int(arOcmd)


##############################################
if arOcmd==1:
    file = open("gramatica.txt")
    variables=file.readline().split()
    file.readline()
    file.readline()

    producciones=[]
    produccionesF=[]
    for index in variables:
        producciones=file.readline().split()
        produccionesF.append(producciones)
        producciones=[]
    #print produccionesF
    file.readline()

    string = file.readline()
    string = string.strip()
    #print string
    file.readline()
    op=file.readline()
    op=int(op)
    #print op
    if op==3:
        #print "AAAAAAAAA"
        numSust = file.readline()
        numDeriv = file.readline()
        numSust = int(numSust)
        numDeriv = int(numDeriv)


################################################
if arOcmd==2:
    variables=[]

    numVar = raw_input('Dame el numero de variables:  ')
    numVar = int(numVar)

    for index in range(1,numVar+1):
        if index==1:
            z=raw_input('Dame la variable inicial:  ')
        else:
            z=raw_input('Dame la variable #%d:  ' %index)
        variables.append(z)
    producciones=[]
    produccionesF=[]
    for index in variables:
        numProd = raw_input('Dame el numero de producciones de %s:  ' %index)
        numProd = int(numProd)
        producciones.append(index)
        for index2 in range(1,numProd+1):
            z=raw_input('Dame la produccion #%s:  ' %index2)
            producciones.append(z)
        produccionesF.append(producciones)
        producciones=[]
    #print produccionesF
    #CFG=produccionesF
    string = raw_input('Dame el string buscado:  ')



    #######################################################################
    #Decision
    #######################################################################
    print "\n"
    print "Escoge una opcion:"
    print "1. Derivacion por la izquierda"
    print "2. Derivacion por la derecha"
    print "3. Todas las derivaciones hasta cierto punto"

    op = raw_input('Ingrese una opcion:  ')
    op=int(op)

    if op==3:
        numSust = raw_input('Dame el numero de sustituciones:  ')
        numDeriv = raw_input('Dame el numero de derivaciones:  ')
        numSust = int(numSust)
        numDeriv = int (numDeriv)




CFG=produccionesF
##################################################
#Pruebas
#################################################
#CFG=produccionesF
#S = ["aAS","a"]
#S = [ "S+S", "S*S", "(S)", "a", "b"]
#S = [ "S+S", "a", "b"]
#A=["SbA","SS","ba"]
#CFG = [["S","aAS","a"],["A","SbA","SS","ba"]]
#CFG =[["S", "S+S", "S*S", "(S)", "a", "b"]]
#CFG =[["S", "S+S", "a", "b"]]
#string = "aabbaa"
#string = "a+b+a"
#string = "aabbaa"
#########################################################
#string = raw_input('Dame el string buscado:  ')

arr=[]
arrCambio=[]
arr2=[]
arrCambio2=[]
arr3=[]
arrCambio3=[]
aux=[]
auxCambio=[]
arrResultado=[]
arrResultadoCambio=[]
arrResultado2=[]
arrResultadoCambio2=[]
arrResultado3=[]
arrResultadoCambio3=[]


for index in range(1,len(produccionesF[0])):
    aux.append([produccionesF[0][0], produccionesF[0][index]])
    auxCambio.append([produccionesF[0][0]+"->"+produccionesF[0][index]])

#print aux
#print auxCambio

"""
for index in S:
    aux.append(['S',index])
    auxCambio.append(['S'+"->"+index])

print aux
print auxCambio
"""

arr.append(aux)
arr2.append(aux)
arr3.append(aux)
arrCambio.append(auxCambio)
arrCambio2.append(auxCambio)
arrCambio3.append(auxCambio)

#print arrCambio




#############################################################################
#Derivacion por la izquierda
############################################################################
if op==1:
    cont = 0
    encontrado=False
    #while cont < 4:
    while encontrado==False:

        arrResultado=[]
        arrResultadoCambio=[]

        ayuda2=[]
        ayuda2Cambio=[]
        largo = len(arr)
        #print largo
        for index in arr[largo-1]:
                aux2 = index[1]
                aux3 = aux2
                ayuda=[]
                ayudaCambio=[]
                ayudaV = True
                cond = True
                for index2 in range(0, len(aux2)):
                    for index3 in CFG:
                        if aux3[index2] == index3[0] and cond==True:
                            cond = False
                            for index4 in range(1,len(index3)):
                                aux3 = aux3[:index2+1].replace(index3[0],index3[index4])+aux3[index2+1:]
                                #print aux3
                                ayuda.append([aux2,aux3])
                                ayudaCambio.append([aux2[index2]+"->"+index3[index4]])
                                ayudaV = False
                                aux3 = aux2


                #print ayuda
                #if len(ayuda)>0:
                 #   arr.append(ayuda)
                if ayudaV == False:
                    ayuda2.extend(ayuda)
                    ayuda2Cambio.extend(ayudaCambio)
                    #arr.append(ayuda2)
                    #print ayuda2
                    #ayuda2=[]
        arr.append(ayuda2)
        arrCambio.append(ayuda2Cambio)
        #print ayuda2
        #print arrCambio
        #print "\n"
        #print arr
        #print "\n\n"
        cont =cont + 1

        vacio=True
        rep = False
        for index in range(0,len(arr)):
            for index2 in range(0,len(arr[index])):
                if arr[index][index2][1] == string and rep == False:
                    arrResultado.append(arr[index][index2])
                    arrResultadoCambio.append(arrCambio[index][index2])
                    #while arr[0][0][0] != arrResultado[len(arrResultado)-1][0]:
                    #print arr[0][0][0]
                    print "Se encontro el string por derivacion a la izquierda"
                    encontrado=True
                    vacio=False
                    rep = True



        #print arrResultado

        if vacio==False:
            while arr[0][0][0] != arrResultado[len(arrResultado)-1][0]:
                for index in range(0,len(arr)):
                    for index2 in range(0,len(arr[index])):
                        if arrResultado[len(arrResultado)-1][0] == arr[index][index2][1]:
                            arrResultado.append(arr[index][index2])
                            arrResultadoCambio.append(arrCambio[index][index2])
                            #print arrResultado
        arrResultado.reverse()
        arrResultadoCambio.reverse()
    #print arr
    #print arrResultado
    #print arrResultadoCambio


    for index in range(0,len(arrResultado)):
        igual=False
        for index2 in range (0,len(arrResultado[index])):
            rojo=False
            for index3 in range(0,len(arrResultado[index][index2])):
                if index2 == 0 and rojo==False:
                    alerta = False
                    for index4 in CFG:
                        if index4[0] == arrResultado[index][index2][index3]:
                            rojo = True
                    if rojo==True:
                            stdout.write(color.RED + arrResultado[index][index2][index3] + color.END)
                    else:
                        stdout.write(arrResultado[index][index2][index3])
                        #alerta=True
                else:
                    stdout.write(arrResultado[index][index2][index3])
                #stdout.write(" = ")
                #stdout.write(arrResultado[index][index2][index3])
            if igual==False:
                stdout.write(" = ")
                igual=True
        stdout.write("  ||  " + arrResultadoCambio[index][0] )
        print  "\n"

    print "\n\n"
    #print CFG


#############################################################################
#Derivacion por la derecha
############################################################################
if op==2:

    cont = 0
    encontrado=False
    #while cont < 4:
    while encontrado==False:

        arrResultado2=[]
        arrResultadoCambio2=[]

        ayuda2=[]
        ayuda2Cambio=[]
        largo = len(arr2)
        #print largo
        for index in arr2[largo-1]:
                aux2 = index[1]
                aux3 = aux2
                ayuda=[]
                ayudaCambio=[]
                ayudaV = True
                cond = True
                lenAux2 = len(aux2)-1
                while lenAux2>=0:
                #for index2 in range(0, len(aux2)):
                    for index3 in CFG:
                        if aux3[lenAux2] == index3[0] and cond==True:
                            cond = False
                            for index4 in range(1,len(index3)):
                                aux3 = aux3[:lenAux2]+aux3[lenAux2:].replace(index3[0],index3[index4])
                                #print aux3
                                ayuda.append([aux2,aux3])
                                ayudaCambio.append([aux2[lenAux2]+"->"+index3[index4]])
                                ayudaV = False
                                aux3 = aux2

                    lenAux2=lenAux2 -1
                #print ayuda
                #if len(ayuda)>0:
                 #   arr.append(ayuda)
                if ayudaV == False:
                    ayuda2.extend(ayuda)
                    ayuda2Cambio.extend(ayudaCambio)
                    #arr.append(ayuda2)
                    #print ayuda2
                    #ayuda2=[]
        arr2.append(ayuda2)
        arrCambio2.append(ayuda2Cambio)
        #print "\n\n\n\n"
        #print arrCambio2
        #print ayuda2
        #print "\n"
        #print arr2
        #print "\n\n"
        cont =cont + 1


        vacio=True
        rep = False
        for index in range(0,len(arr2)):
            for index2 in range(0,len(arr2[index])):
                if arr2[index][index2][1] == string and rep == False:
                    arrResultado2.append(arr2[index][index2])
                    arrResultadoCambio2.append(arrCambio2[index][index2])
                    #while arr[0][0][0] != arrResultado[len(arrResultado)-1][0]:
                    #print arr[0][0][0]
                    print "Se encontro el string por derivacion la derecha"
                    encontrado=True
                    vacio=False
                    rep = True

            if vacio==False:
                while arr2[0][0][0] != arrResultado2[len(arrResultado2)-1][0]:
                    for index in range(0,len(arr2)):
                        for index2 in range(0,len(arr2[index])):
                            if arrResultado2[len(arrResultado2)-1][0] == arr2[index][index2][1]:
                                arrResultado2.append(arr2[index][index2])
                                arrResultadoCambio2.append(arrCambio2[index][index2])
                                #print arr2[index][index2]

            arrResultado2.reverse()
            arrResultadoCambio2.reverse()

    #print arr2
    #print '\n'
    #print arrCambio



    for index in range(0,len(arrResultado2)):
        igual=False
        for index2 in range (0,len(arrResultado2[index])):
            rojo=False
            for index3 in range(0,len(arrResultado2[index][index2])):
                falta=False
                if index2 == 0 and rojo==False:
                    alerta = False
                    for index4 in CFG:
                        if index4[0] == arrResultado2[index][index2][index3]:
                            for index5 in range(index3+1, len(arrResultado2[index][index2])):
                                for index6 in CFG:
                                    #print index6[0] + "      1"
                                    #print arrResultado2[index][index2][index5] + "      2"
                                    if index6[0] == arrResultado2[index][index2][index5]:
                                        #print index4[0]
                                        #print arrResultado2[index][index2][index5]
                                        falta=True
                            if falta==False:
                                rojo = True
                    if rojo==True:
                            stdout.write(color.RED + arrResultado2[index][index2][index3] + color.END)
                    else:
                        stdout.write(arrResultado2[index][index2][index3])
                        #alerta=True
                else:
                    stdout.write(arrResultado2[index][index2][index3])
                #stdout.write(" = ")
                #stdout.write(arrResultado[index][index2][index3])
            if igual==False:
                stdout.write(" = ")
                igual=True
        stdout.write("  ||  " + arrResultadoCambio2[index][0] )
        print  "\n"

    print "\n\n"
    #print CFG

    #print arrResultado2




#############################################################################
#Derivacion General
############################################################################

#################################################
if op==3:
    arr=[]
    arrCambio=[]
    arr2=[]
    arrCambio2=[]
    arr3=[]
    arrCambio3=[]
    aux=[]
    auxCambio=[]
    auxID=[]
    auxPos=[]

    id=1

    arrResultado=[]
    arrResultadoCambio=[]
    arrResultado2=[]
    arrResultadoCambio2=[]
    arrResultado3=[]
    arrResultadoCambio3=[]



    """
    for index in S:
        aux.append(['S',index])
        auxCambio.append(['S'+"->"+index])
        auxID.append([id,0])
        id=id+1
        auxPos.append([0])
    """
    for index in range(1,len(produccionesF[0])):
        aux.append([produccionesF[0][0], produccionesF[0][index]])
        auxCambio.append([produccionesF[0][0]+"->"+produccionesF[0][index]])
        auxID.append([id,0])
        id=id+1
        auxPos.append([0])

    arr.append(aux)
    arr2.append(aux)
    arr3.append(aux)
    arrCambio.append(auxCambio)
    arrCambio2.append(auxCambio)
    arrCambio3.append(auxCambio)



    ###
    arrID=[]
    arrPos=[]
    arrID.append(auxID)
    arrPos.append(auxPos)
    ###

    #print arrID
    #print arrPos

    #############################################################################
    #Derivacion General
    ############################################################################

    cont = 0
    while cont < numSust-1:

        ayuda2=[]
        ayuda2Cambio=[]
        ayudaID2=[]
        ayudaPos2=[]
        largo = len(arr)
        #print largo
        for index in range(0,len(arr[largo-1])):
                aux2 = arr[largo-1][index][1]
                #print aux2
                aux3 = aux2
                ayuda=[]
                ayudaCambio=[]
                ayudaID=[]
                ayudaPos=[]
                ayudaV = True
                cond = True
                for index2 in range(0, len(aux2)):
                    for index3 in CFG:
                        if aux3[index2] == index3[0]:
                            cond = False
                            #ayudaPos.append([index2])
                            for index4 in range(1,len(index3)):
                                #aux3 = aux3[:index2+1].replace(index3[0],index3[index4])+aux3[index2+1:]
                                aux3 = list(aux3)
                                aux3[index2] = index3[index4]
                                aux3=''.join(aux3)
                                #print aux3
                                ayuda.append([aux2,aux3])
                                ayudaCambio.append([aux2[index2]+"->"+index3[index4]])
                                ayudaID.append([id,arrID[largo-1][index][0]])
                                ayudaPos.append([index2])
                                ayudaV = False
                                aux3 = aux2
                                id=id+1
                #print ayuda
                #print ayudaPos
                #print "\n\n"
                #print ayuda
                #if len(ayuda)>0:
                 #   arr.append(ayuda)
                if ayudaV == False:
                    ayuda2.extend(ayuda)
                    ayuda2Cambio.extend(ayudaCambio)
                    ayudaID2.extend(ayudaID)
                    ayudaPos2.extend(ayudaPos)
                    #arr.append(ayuda2)
                    #print ayuda2
                    #ayuda2=[]
        arr.append(ayuda2)
        arrCambio.append(ayuda2Cambio)
        arrID.append(ayudaID2)
        arrPos.append(ayudaPos2)
        #print ayuda2
        #print arrCambio
        #print "\n"
        #print arrID
        #print arrPos
        #print "\n\n"
        cont =cont + 1



    #print arr
    #print arrPos

    ###########################################
    contTotal =0
    for index in arr:
        for index2 in index:
            if index2[1] == string:
                contTotal = contTotal+1


    contTotal=1
    arrResultadoFinal=[]
    arrResultadoFinalID=[]
    arrResultadoFinalCambio=[]
    arrResultadoFinalPos=[]
    while contTotal>0:
        vacio=True
        rep = False
        arrResultadoID=[]
        arrResultadoPos=[]
        for index in range(0,len(arr)):
            for index2 in range(0,len(arr[index])):
                if arr[index][index2][1] == string and rep == False:
                    arrResultado.append(arr[index][index2])
                    arrResultadoCambio.append(arrCambio[index][index2])
                    arrResultadoID.append(arrID[index][index2])
                    arrResultadoPos.append(arrPos[index][index2])
                    #while arr[0][0][0] != arrResultado[len(arrResultado)-1][0]:
                    #print arr[0][0][0]

                    #############################################################
                    while arr[0][0][0] != arrResultado[len(arrResultado)-1][0]:
                        for index in range(0,len(arrID)):
                            for index2 in range(0,len(arrID[index])):
                                if arrResultadoID[len(arrResultado)-1][1] == arrID[index][index2][0]:
                                    arrResultado.append(arr[index][index2])
                                    arrResultadoID.append(arrID[index][index2])
                                    arrResultadoPos.append(arrPos[index][index2])
                                    arrResultadoCambio.append(arrCambio[index][index2])

                    arrResultado.reverse()
                    arrResultadoID.reverse()
                    arrResultadoCambio.reverse()
                    arrResultadoPos.reverse()
                    arrResultadoFinal.append(arrResultado)
                    arrResultadoFinalID.append(arrResultadoID)
                    arrResultadoFinalCambio.append(arrResultadoCambio)
                    arrResultadoFinalPos.append(arrResultadoPos)
                    #print arrResultado
                    #print arrResultadoID
                    #print arrResultadoCambio
                    #print arrResultadoPos

                    #print "\n\n"
                    arrResultado=[]
                    arrResultadoID=[]
                    arrResultadoCambio=[]
                    arrResultadoPos=[]
                    ############################################################

                    #print "Se encontro el string"
                    vacio=False
                    #rep = True

        #print arrResultadoID



        #arrResultado.reverse()
        #arrResultadoCambio.reverse()
        #arrResultadoID.reverse()
        #print arrResultado
        #print arrResultadoID
        #print "\n\n"
        contTotal=contTotal-1
        #print arrResultadoCambio
        #print arr
    ############################################

    #print arrResultadoFinal
    #print len(arrResultadoFinal)
    niTeMolestes=False
    if len(arrResultadoFinal)==0:
        print "\n"
        print "No hay derivaciones para esta N"
        niTeMolestes=True

    #for index in range(0,len(arrResultadoFinal)):
    if niTeMolestes==False:
        for index in range(0,numDeriv):
            print ("Solucion: %d"  %index)
            for index2 in range(0,len(arrResultadoFinal[index])):
                aa=False
                for index3 in range(0,len(arrResultadoFinal[index][index2])):
                    for index4 in range(0,len(arrResultadoFinal[index][index2][index3])):
                        if index3 == 0 and index4 == arrResultadoFinalPos[index][index2][0]:
                            stdout.write(color.RED + arrResultadoFinal[index][index2][index3][index4]+ color.END)
                        else:
                            stdout.write(arrResultadoFinal[index][index2][index3][index4])
                    if aa==False:
                        stdout.write(" = ")
                        aa=True
                stdout.write("  ||  ")
                stdout.write(arrResultadoFinalCambio[index][index2][0])
                print "\n"
            print "\n\n"




    #print CFG
    #print arrPos
    #print arrID
