from enum import auto
from AnalizadorLexico import *
from Estado import *
import copy
from transicion import *
from AFN import *
from subconjuntos import *
from operator import attrgetter
import graphviz 


def eClosure(self,states):
    while True:
        siguiente =[]    
        for s in states:
            if s.tipo == 3 and s not in siguiente:
                siguiente.append(s)
                for i in s.transiciones:
                    if i.trans_label == "E":
                        #estado =list( filter(lambda x: x.label == i.destino,states))
                        estado = None
                        for st in self.maquinas[0].estados:
                            if st.label == i.destino:
                                estado = st
                                break
                        if estado is not None: 
                            if estado not in siguiente:
                                if s not in siguiente:
                                    siguiente.append(s)
                                siguiente.append(estado)
                        elif s not in siguiente:
                            siguiente.append(s)                    
                                
                    elif s not in siguiente:
                        siguiente.append(s)


        siguiente.sort(key =attrgetter("label"),reverse=False)
        if states == siguiente:
            return siguiente  
        states = siguiente
    return siguiente



def subset(self,afn):
    object = Parser(self.regex)
    alpha = object.mapa_simbolos()
    alpha.sort()
    afd = []
    destados = [self.eClosure([afn.estados[0]])]
    cont, indicador = 0,0
    while indicador < len(destados):
        transi = []
        cont = indicador + 1
        for c in alpha:
            temp = self.eClosure(self.move(destados[indicador],c))
            if temp in destados:
                arr = list(filter(lambda x: x == temp,destados))
                pos = destados.index(arr[0])
                transi.append(transcision("s"+str(pos),c))
            else:
                if len(temp)== 0:
                    cont =cont -1
                    continue
                if indicador > 0:
                    transi.append(transcision("s"+str(len(destados)),c))
                else:
                    transi.append(transcision("s"+str(cont),c))
                    destados.append(temp)
                    cont =cont + 1

        tipo3 = False
        sf = afn.estados[-1].label

        for j in destados[indicador]:
            if j.label == sf:
                tipo3 = True
                break
        if indicador == 0:
            afd.append(estado("s"+str(indicador),transi,1))
        else:
            afd.append(estado("s"+str(indicador),transi,3 if tipo3 else 2))
        indicador =indicador +1
    return nfa(afd,[],alpha)
    

def simul2(self,cadena,afd):
    estados = []
    estados.append(afd.estados[0])
    cont = 1
    for c in cadena:
        estados = self.move2(estados,c,afd)
        cont +=1
    return estados[0].tipo ==3

def move2(self,states,chr,maquina):
    response = []
    for s in states:
        for i in s.transaccion:
            if i.trans_label == chr:
                estado = None
                for st in maquina.estados:
                    if st.label == i.destino:
                        estado = st    
                if estado is not None:
                    if estado not in response:
                        response.append(estado)
                elif s not in response:
                    response.append(s)

    return response






    
