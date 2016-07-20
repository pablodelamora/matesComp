import itertools
file = open("NFA.txt")
Q = file.readline().split()
sigma = file.readline().split()
file.readline()

####################################################################
#Funciones
def agregaConjunto (vacio, conjunto2):
    for i in conjunto2:
        i += [vacio]
    return conjunto2

def potencia(conjunto):
    if not conjunto: return [[]]

    vacio = conjunto[0]

    conjunto2 = conjunto[1:]
    return potencia(conjunto2) + agregaConjunto(vacio, potencia(conjunto2))


######################################################################


NFA = []
for index in range((len(Q))+1):
    NFA.append(file.readline().split())

file.readline()
inicial = file.readline()
inicial = inicial.strip()
terminal = file.readline()
terminal = terminal.strip()

QF = []
#for  i in xrange(1, len(Q)+1):
#    #QF = QF + list(itertools.combinations(Q,i))
#    QF.extend(list(itertools.combinations(Q,i)))

QF = potencia(Q)

for index in range(0,len(QF)):
    QF[index].sort()
    XX = " ".join(str(x) for x in QF[index])
    QF[index] = XX
    QF[index]=QF[index].replace(' ',',')

QF.sort()

#DFA = []
DFA = [[] for x in xrange(len(QF))]
for index in range(0,len(DFA)):
    for index2 in range(0,len(sigma)+1):
        DFA[index].append('*')




cont =0


for index in QF:
    (DFA[cont])[0] = index
    cont +=1

for index in DFA:
    #if index[0] == inicial:
        for index2 in NFA:
            if index2[0] == index[0]:
                cont = 0
                for index3 in index2:
                    index[cont] = index3
                    cont+=1




aux=[]
for index in DFA:
    if len(index[0])>2:
        aux.append(index[0].split(','))

####Hasta aqui corre perfecto



################Error
aux2=[]
auxP=[]
aux3=[]
aux4=[]
for index in aux:
    aux2=[]
    for index2 in index:
        for index3 in NFA:
            if index2 == index3[0]:
                if len(aux2)==0:
                    for index4 in index3:
                        aux2.append(index4.split(','))
                        #print aux2
                else:
                    i=0
                    for index5 in aux2:
                            index5.extend(index3[i].split(','))
                            i+=1
                            #print aux2
    auxP.append(aux2)
    #aux2=[]
    #auxP2.append(auxP)        
####################Error


for index in auxP:
    aux3=[]
    for index2 in index:
        aux3.append(list(set(index2)))
    aux4.append(aux3)




for index in aux4:
    for index2 in index:
        index2 =index2.sort()


for index in aux4:
    for index2 in index:
        if len(index2)>1:
            if '*' in index2:
                index2.remove('*')




for index in aux4:
    for index2 in range(0,len(index)):
        XX = " ".join(str(x) for x in index[index2])
        index[index2] = XX
        index[index2] = index[index2].replace(' ',',')



for index in DFA:
    if index[0] =='':
        index[0]='*'
        

for index in aux4:
    for index2 in DFA:
        if index[0] == index2[0]:
            for index3 in range(0,len(index)):
                index2[index3]=index[index3]


for index in DFA:
    print index
                


#print aux
#print aux2
#print aux3
#print aux4
#print auxP
#print auxP2
#print NFA
#print DFA
#print NFA
#print QF








    
